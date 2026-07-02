from task import Task


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, task):
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)

    def remove_task(self, task_id):

        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def search_task(self, task_id):

        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def show_tasks(self):
        return self.tasks
