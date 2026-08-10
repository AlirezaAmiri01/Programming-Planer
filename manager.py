import storage
from storage import save_tasks, load_tasks
from datetime import date


class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()
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
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[index]
                storage.save_tasks(self.tasks)
                return True
        return False

    def search_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def show_tasks(self):
        return self.tasks.copy()

    def edit_title(self, task_id, new_title):
        for task in self.tasks:
            if task.id == task_id:
                task.title = new_title
                storage.save_tasks(self.tasks)
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
        storage.save_tasks(self.tasks)

    def sort_by_id(self):
        self.tasks.sort(key=lambda task: task.id)
        storage.save_tasks(self.tasks)

    def sort_by_status(self):
        self.tasks.sort(key=lambda task: task.done)
        storage.save_tasks(self.tasks)

    def sort_by_deadline(self):
        self.tasks.sort(
            key=lambda task: task.deadline if task.deadline else date.max)
        storage.save_tasks(self.tasks)

    def reset_all_tasks(self):
        self.tasks = []
        self.next_id = 1
        storage.save_tasks(self.tasks)

    def update_task(self, updated_task):
        for index, task in enumerate(self.tasks):
            if task.id == updated_task.id:
                self.tasks[index] = updated_task
                break
        storage.save_tasks(self.tasks)
