"""Problem: Create a simple event scheduler."""

# Problem:
# Store events and display them in order.

from datetime import datetime


class EventScheduler:
    def __init__(self):
        self.events = []

    def add_event(self, title, date_text):
        event_date = datetime.strptime(date_text, "%Y-%m-%d")
        self.events.append({"title": title, "date": event_date})

    def list_events(self):
        for event in sorted(self.events, key=lambda item: item["date"]):
            print(event["date"].date(), "-", event["title"])


# Solution:
scheduler = EventScheduler()
scheduler.add_event("Project Review", "2026-06-10")
scheduler.add_event("Meeting", "2026-06-08")
scheduler.list_events()

# Logic:
# 1. Store each event with a parsed date.
# 2. Sort events by date before showing them.
# 3. Print the schedule in time order.

# Explanation:
# This is a small real-world style application of classes and dates.
