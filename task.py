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
        created = self.created_at.strftime("%Y/%m/%m/%d")
        deadline = self.deadline.strftime("%Y/%m/%d")

        return (
            f"id          : {self.id}\n"
            f"title       : {self.title}\n"
            f"description : {self.description}\n"
            f"status      : {status}\n"
            f"priority    : {self.priority}\n"
            f"created_at  : {created}\n"
            f"deadline    : {deadline}"
        )

    def mark_done(self):
        self.done = True

    def mark_pending(self):
        self.done = False
