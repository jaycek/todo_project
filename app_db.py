import sqlite3
from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)
DATABASE = 'todos.db'


def get_db():
    """Open a fresh connection for each request."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def find_todo(todo_id):
    """Return the todo row with this id, or 404 if missing."""
    conn = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
        row = cursor.fetchone()
    except sqlite3.Error as e:
        app.logger.error(f"DB error in find_todo({todo_id}): {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    if row is None:
        abort(404)
    return row


# READ
@app.route('/')
def get_todos():
    conn = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todos ORDER BY id ASC")
        todos = cursor.fetchall()
    except sqlite3.Error as e:
        app.logger.error(f"DB error in get_todos: {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    return render_template('todos.html', todos=todos)


# CREATE
@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task', '').strip()
    if not task:
        return redirect(url_for('get_todos'))

    conn = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO todos (task) VALUES (?)", (task,))
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        app.logger.error(f"DB error in add_todo: {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    return redirect(url_for('get_todos'))


# UPDATE
@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo = find_todo(todo_id)   # handles its own errors + 404

    if request.method == 'POST':
        task = request.form.get('task', '').strip()
        if not task:
            return redirect(url_for('get_todos'))

        conn = None
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE todos SET task = ? WHERE id = ?",
                (task, todo_id)
            )
            conn.commit()
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            app.logger.error(f"DB error in edit_todo({todo_id}): {e}")
            abort(500)
        finally:
            if conn:
                conn.close()
        return redirect(url_for('get_todos'))

    return render_template('edit.html', todo=todo)


# DELETE
@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    todo = find_todo(todo_id)   # handles its own errors + 404

    conn = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        app.logger.error(f"DB error in delete_todo({todo_id}): {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    return redirect(url_for('get_todos'))


# Friendly error pages instead of Flask's default gray screens
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)