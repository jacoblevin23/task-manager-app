# This file is part of the Task Manager application.
# It provides the Database class for interacting with the MySQL database.
# The Database class includes methods for inserting, fetching, updating, and deleting tasks.
# It uses the mysql-connector-python library to connect to the MySQL database.
# The database connection settings are defined in the config/config.py file.
# The Database class uses a context manager to ensure that the database connection is properly closed when no longer needed.

import mysql.connector
from mysql.connector import Error
from app.utils import dict_from_cursor
from config.config import DB_CONFIG


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)

    def insert_task(self, title, description, due_date, priority, status, created_at):
        query = """
            INSERT INTO tasks (title, description, due_date, priority, status, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (title, description, due_date, priority, status, created_at))
        self.conn.commit()
        return self.cursor.lastrowid

    def fetch_tasks(self, filters=None):
        query = "SELECT * FROM tasks WHERE 1=1"
        values = []

        if filters:
            if "status" in filters:
                query += " AND status = %s"
                values.append(filters["status"])
            if "priority" in filters:
                query += " AND priority = %s"
                values.append(filters["priority"])
            if "due_date" in filters:
                query += " AND due_date = %s"
                values.append(filters["due_date"])

        query += " ORDER BY due_date ASC"

        self.cursor.execute(query, tuple(values))
        return self.cursor.fetchall()

    def update_task(self, task_id, **fields):
        updates = []
        values = []

        for key, val in fields.items():
            updates.append(f"{key} = %s")
            values.append(val)

        if not updates:
            return

        query = f"UPDATE tasks SET {', '.join(updates)} WHERE task_id = %s"
        values.append(task_id)

        self.cursor.execute(query, tuple(values))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
        self.conn.commit()

    def __del__(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
