"""Problem: Create a simple TODO manager."""

# Problem:
# Manage a small to-do list using a class.


class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        return f"Added: {task}"

    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            return "Invalid task number."
        self.tasks[index]["done"] = True
        return f"Completed: {self.tasks[index]['task']}"

    def show_tasks(self):
        for i, item in enumerate(self.tasks, start=1):
            status = "Done" if item["done"] else "Pending"
            print(f"{i}. {item['task']} - {status}")


# Solution:
todo = TodoManager()
print(todo.add_task("Learn Python"))
print(todo.add_task("Practice OOP"))
print(todo.complete_task(0))
todo.show_tasks()

# Logic:
# 1. Store tasks in a list.
# 2. Keep each task with a done/not done status.
# 3. Update and display the list with methods.

# Explanation:
# This is a tiny project that feels like a real app feature.
