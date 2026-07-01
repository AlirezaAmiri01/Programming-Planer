from task import Task


class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):

        self.tasks.append(task)

    def remove_task(self, title):

        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def search_task(self, title):

        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def show_tasks(self):
        return self.tasks
