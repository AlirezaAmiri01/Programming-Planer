from task import Task
import storage


class TaskManager:

    class TaskManager:

        def __init__(self):
            self.tasks = storage.load_tasks()

            if self.tasks:
                self.next_id = max(task.id for task in self.tasks) + 1
            else:
                self.next_id = 1

    def add_task(self, task):
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        storage.save_tasks(self.tasks)

    def remove_task(self, task_id):

        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                storage.save_tasks(self.tasks)
                return True
        return False

    def search_task(self, task_id):

        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def show_tasks(self):
        return self.tasks

    def edit_title(self, task_id, new_title):
        for task in self.tasks:
            if task.id == task_id:
                task.title = new_title
                return True
        return False

    def edit_description(self, task_id, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                storage.save_tasks(self.tasks)
                return True
        return False

    def edit_priority(self, task_id, new_priority):
        for task in self.tasks:
            if task.id == task_id:
                task.priority = new_priority
                storage.save_tasks(self.tasks)
                return True
        return False

    def edit_deadline(self, task_id, new_deadline):
        for task in self.tasks:
            if task.id == task_id:
                task.deadline = new_deadline
                storage.save_tasks(self.tasks)
                return True
        return False

    def mark_task_done(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_done()
                storage.save_tasks(self.tasks)
                return True

        return False

    def mark_task_pending(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_pending()
                storage.save_tasks(self.tasks)
                return True

        return False

    def sort_by_priority(self):
        self.tasks.sort(key=lambda task: task.priority)

    def sort_by_title(self):
        self.tasks.sort(key=lambda task: task.title)

    def sort_by_create_at(self):
        self.tasks.sort(key=lambda task: task.create_at)

    def sort_by_deadline(self):
        self.tasks.sort(key=lambda task: task.deadline)
