#  This script serves as the entry point for the TaskCLI application.
# It initializes the TaskCLI class and starts the command line interface for managing tasks.

from app.cli import TaskCLI

if __name__ == "__main__":
    app = TaskCLI()
    app.run()
