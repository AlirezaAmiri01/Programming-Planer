from datetime import date


class Task:
    def __init__(self, title, description, priority):
        self.id = None
        self.done = False
        self.created_at = date.today()
        self.title = title
        self.description = description
        self.priority = priority

    def __str__(self):
        status = ""
        if self.done == True:
            status = "Done"
        else:
            status = "pending"

        return f"id          : {self.id}\ntitle       : {self.title}\ndescription : {self.description}\nstatus      : {status}\npriority    : {self.priority}\ncreated_at  : {self.created_at} "

    def mark_done(self):
        self.done = True

    def mark_pending(self):
        self.done = False
