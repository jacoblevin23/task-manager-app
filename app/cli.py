# This code implements a Command Line Interface (CLI) for managing tasks using the TaskManager class.
# It allows users to add, list, update, complete, and delete tasks interactively.

from app.task_manager import TaskManager
from app.db import Database
from datetime import datetime

class TaskCLI:
    def __init__(self):
        db = Database()
        self.manager = TaskManager(db)

    def run(self):
        while True:
            self.print_menu()
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.list_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.complete_task()
            elif choice == '5':
                self.delete_task()
            elif choice == '6':
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def print_menu(self):
        print("\n--- Task Manager CLI ---")
        print("1. Add New Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

    def add_task(self):
        try:
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            priority = input("Priority (Low/Medium/High): ")
            task_id = self.manager.add_task(title, description, due_date, priority)
            print(f"Task added with ID {task_id}")
        except Exception as e:
            print(f"Error adding task: {e}")

    def list_tasks(self):
        print("Filter tasks (leave blank to skip):")
        status = input("Status [Pending/In Progress/Completed]: ").strip()
        priority = input("Priority [Low/Medium/High]: ").strip()
        due_date = input("Due Date (YYYY-MM-DD): ").strip()

        filters = {}
        if status: filters["status"] = status
        if priority: filters["priority"] = priority
        if due_date: filters["due_date"] = due_date

        try:
            tasks = self.manager.get_all_tasks(filters)
            if not tasks:
                print("No tasks found.")
            for task in tasks:
                print(task)
        except Exception as e:
            print(f"Error fetching tasks: {e}")

    def update_task(self):
        try:
            task_id = int(input("Enter Task ID to update: "))
            print("Leave fields blank to skip updating them.")
            title = input("New Title: ")
            description = input("New Description: ")
            due_date = input("New Due Date (YYYY-MM-DD): ")
            priority = input("New Priority (Low/Medium/High): ")
            status = input("New Status (Pending/In Progress/Completed): ")

            fields = {k: v for k, v in {
                "title": title,
                "description": description,
                "due_date": due_date,
                "priority": priority,
                "status": status
            }.items() if v}

            self.manager.update_task(task_id, **fields)
            print("Task updated.")
        except Exception as e:
            print(f"Error updating task: {e}")

    def complete_task(self):
        try:
            task_id = int(input("Enter Task ID to mark as completed: "))
            self.manager.mark_task_completed(task_id)
            print("Task marked as completed.")
        except Exception as e:
            print(f"Error marking task complete: {e}")

    def delete_task(self):
        try:
            task_id = int(input("Enter Task ID to delete: "))
            self.manager.delete_task(task_id)
            print("Task deleted.")
        except Exception as e:
            print(f"Error deleting task: {e}")
