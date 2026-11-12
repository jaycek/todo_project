# Todo Project -- Flask CRUD Application

A simple Todo application built with **Flask**, developed in two
versions to demonstrate how data can be managed using Python collections
and a relational database.

## Project Versions

### 1. List-Based Version

The first version stores todo items in a Python list. It demonstrates
the basic CRUD workflow without using a database.

### 2. SQLite Database Version

The second version stores todo items in an **SQLite** database. This
makes the data persistent, so todo items remain available after the
application is restarted.

## Features

-   **Create** -- Add a new todo item.
-   **Read** -- View the list of todo items.
-   **Update** -- Edit an existing todo item.
-   **Delete** -- Remove a todo item.
-   Two data-storage approaches: Python list and SQLite.
-   HTML pages rendered using the **Jinja2** template engine.
-   Separate CSS stylesheet for the user interface.
-   Flask routes to handle application requests and CRUD operations.

## Tech Stack

-   **Python**
-   **Flask** -- Web application framework
-   **SQLite** -- Database used in the database-backed version
-   **HTML5 and CSS3** -- Page structure and styling
-   **Jinja2** -- Template rendering (integrated with Flask)

## Project Structure

``` text
todo_project/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── edit.html
│   └── todos.html
│
├── app_db.py
├── init_db.py
├── main.py
└── todos.db
```

### Important Files

  -----------------------------------------------------------------------
  File / Folder                       Purpose
  ----------------------------------- -----------------------------------
  `main.py`                           Flask application for the
                                      list-based version.

  `app_db.py`                         Flask application for the
                                      SQLite-backed version.

  `init_db.py`                        Initializes the SQLite database and
                                      creates the required table.

  `todos.db`                          SQLite database file containing
                                      todo records.

  `templates/`                        Contains the Jinja2 HTML templates.

  `templates/todos.html`              Displays the todo list and provides
                                      the main interface.

  `templates/edit.html`               Provides the interface for editing
                                      a todo item.

  `static/style.css`                  Contains the application's CSS
                                      styles.
  -----------------------------------------------------------------------

## Run Locally

### 1. Clone the repository

``` bash
git clone <your-repository-url>
cd todo_project
```

### 2. Create and activate a virtual environment (recommended)

On Windows PowerShell:

``` powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

On macOS / Linux:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Flask

``` bash
pip install Flask
```

### 4. Run the list-based version

``` bash
python main.py
```

Open the local address shown in the terminal (typically
`http://127.0.0.1:5000/`).

### 5. Run the SQLite version

If the database has not yet been initialized, run:

``` bash
python init_db.py
```

Then start the database-backed application:

``` bash
python app_db.py
```

If the application uses a different run configuration or port, follow
the settings in `app_db.py`.

## Deployment

The Flask application was deployed using
**[PythonAnywhere](https://www.pythonanywhere.com/)**.

## Learning Outcomes

This project provided practical experience with:

-   Building web applications using Flask.
-   Defining routes and handling HTTP requests.
-   Implementing Create, Read, Update and Delete (CRUD) operations.
-   Understanding the difference between in-memory data and persistent
    database storage.
-   Connecting a Flask application to an SQLite database.
-   Rendering dynamic HTML using Jinja2 templates.
-   Organizing static files and templates in a Flask project.
-   Styling web pages with CSS.
-   Deploying a Flask application to a hosting platform.

------------------------------------------------------------------------

*Built as a hands-on project to practise Flask fundamentals and
database-backed web development.*
