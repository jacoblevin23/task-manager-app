# This module defines a Task class for managing tasks in a task management application.
## The Task class includes attributes for task ID, title, description, due date, priority, status, and creation date.
# It provides methods to mark a task as completed, update task details, convert the task to a dictionary, and represent the task as a string.
# The due date can be provided as a string or a datetime object, and the class handles task status updates and priority levels.
# The created_at attribute defaults to the current date and time if not provided.
# The class also includes a method to convert the task to a dictionary format for easy serialization or storage.

from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date, priority, status="Pending", created_at=None):
        self.task_id = task_id
        self.title = title
        self.description = description

        # Expected as a string or datetime object
        self.due_date = due_date 

        # "Low", "Medium", "High"
        self.priority = priority

        # "Pending", "In Progress", "Completed"  
        self.status = status      

        self.created_at = created_at or datetime.now()

    def mark_completed(self):
        self.status = "Completed"

    def update(self, title=None, description=None, due_date=None, priority=None, status=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if priority is not None:
            self.priority = priority
        if status is not None:
            self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": str(self.due_date),
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return f"[{self.task_id}] {self.title} - {self.status} (Due: {self.due_date}, Priority: {self.priority})"
