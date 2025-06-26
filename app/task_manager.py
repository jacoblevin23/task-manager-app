# This module manages tasks in the application.
# It provides methods to add, retrieve, update, delete, and mark tasks as completed.
# It uses the Task class to represent individual tasks and interacts with the Database class for data persistence
# through a MySQL database.
# It handles task creation with attributes like title, description, due date, priority, and status.
# It also includes methods for filtering tasks based on status, priority, and due date.
# It uses the datetime module to handle task creation timestamps.
# It is designed to be used in conjunction with a command-line interface or a web application.

from app.task import Task
from datetime import datetime
from app.db import Database

class TaskManager:
    def __init__(self, db: Database):
        self.db = db

    def add_task(self, title, description, due_date, priority):
        created_at = datetime.now()
        task_id = self.db.insert_task(title, description, due_date, priority, "Pending", created_at)
        return task_id

    def get_all_tasks(self, filters=None):
        rows = self.db.fetch_tasks(filters)
        return [Task(**row) for row in rows]

    def update_task(self, task_id, **kwargs):
        self.db.update_task(task_id, **kwargs)

    def delete_task(self, task_id):
        self.db.delete_task(task_id)

    def mark_task_completed(self, task_id):
        self.db.update_task(task_id, status="Completed")