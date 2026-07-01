from datetime import date


class Task:
    def __init__(self, title, description, priority):
        self.done = False
        self.created_at = date.today()
        self.title = title
        self.description = description
        self.priority = priority

    def mark_done(self):
        self.done = True

    def mark_pending(self):
        self.done = False
