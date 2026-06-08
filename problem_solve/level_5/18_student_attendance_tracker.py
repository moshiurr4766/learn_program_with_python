"""Problem: Track student attendance."""

# Problem:
# Mark attendance and produce a summary.


class AttendanceTracker:
    def __init__(self):
        self.records = {}

    def mark_present(self, name):
        self.records[name] = self.records.get(name, 0) + 1

    def summary(self):
        return self.records


# Solution:
tracker = AttendanceTracker()
tracker.mark_present("Moshiur")
tracker.mark_present("Moshiur")
tracker.mark_present("Nadia")
print(tracker.summary())

# Logic:
# 1. Use a dictionary to count attendance.
# 2. Increase the count when a student is present.
# 3. Return the summary at the end.

# Explanation:
# Counting patterns show up often in small management tools.
