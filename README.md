# 📝 Task Manager CLI App (Python + MySQL)

This is a command-line Task Management Application built with Python 3 and MySQL. It allows users to manage their daily tasks through a simple yet powerful interface, demonstrating principles of object-oriented programming (OOP), database interaction, and clean modular design.

---

## Features

- Add new tasks with title, description, due date, and priority
- List all tasks with optional filtering (by status, priority, or due date)
- Update task details
- Mark tasks as completed
- Delete tasks
- Tasks are stored persistently in a MySQL database
- Clean command-line interface (CLI)
- Follows Python OOP best practices
- Input validation and error handling

---

## Technologies Used

- **Python 3**
- **MySQL** (with raw SQL)
- **mysql-connector-python** for DB connectivity

---

## Steps in Setting Up MySQL Database

### 1. Make sure MySQL server is running locally.

Then run (on your command line):
mysql -u root < data/init_db.sql
This will create the database task_db and the tasks table.

### 3. Configure Database Access
Edit the file config/config.py:

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",  # Replace with your MySQL password if set
    "database": "task_db"
}

### 4. Install Dependencies
Ensure you’re using Python 3.8+

pip install -r requirements.txt

### 5. Run the Application
From the root of the project directory:

python3 main.py

You will see a command-line menu. Follow the prompts to interact with the task manager.



