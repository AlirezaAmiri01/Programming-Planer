from datetime import date


class Task:
    def __init__(self, title, description, priority, deadline):
        self.id = None
        self.done = False
        self.created_at = date.today()
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline

    def __str__(self):
        status = ""
        if self.done == True:
            status = "Done"
        else:
            status = "pending"

        return f"\nid          : {self.id}\n\ntitle       : {self.title}\n\ndescription : {self.description}\n\nstatus      : {status}\n\npriority    : {self.priority}\n\ncreated_at  : {self.created_at}\n\ndeadline    : {self.deadline} "

    def mark_done(self):
        self.done = True

    def mark_pending(self):
        self.done = False
