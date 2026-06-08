"""Problem: Sort tasks by priority."""

# Problem:
# Put tasks in priority order.

tasks = [
    {"task": "Email reply", "priority": 2},
    {"task": "Fix bug", "priority": 1},
    {"task": "Write report", "priority": 3},
]

# Solution:
sorted_tasks = sorted(tasks, key=lambda item: item["priority"])
for task in sorted_tasks:
    print(task["priority"], task["task"])

# Logic:
# 1. Keep tasks as dictionaries.
# 2. Sort them by the priority field.
# 3. Print them in order.

# Explanation:
# Sorting by a key is one of the most common data tasks.
