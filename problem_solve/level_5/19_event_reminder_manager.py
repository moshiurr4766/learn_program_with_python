"""Problem: Manage event reminders."""

# Problem:
# Store reminders and show which ones are due.

from datetime import date


class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, title, due_date):
        self.reminders.append({"title": title, "due_date": due_date})

    def due_today(self, today):
        return [item for item in self.reminders if item["due_date"] <= today]


# Solution:
manager = ReminderManager()
manager.add_reminder("Pay bill", date(2026, 6, 8))
manager.add_reminder("Project demo", date(2026, 6, 10))
print(manager.due_today(date(2026, 6, 8)))

# Logic:
# 1. Store reminders with due dates.
# 2. Compare dates with today's date.
# 3. Return the reminders that are due.

# Explanation:
# Date filtering is a useful real-world list operation.
