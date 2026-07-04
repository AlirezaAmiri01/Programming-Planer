from task import Task
from manager import TaskManager
import storage
from datetime import date


def menu():
    print("=====WLCOME TO MENU=====")
    print("1.Add Task")
    print("2.Remove Task")
    print("3.Show Tasks")
    print("4.Search Task")
    print("0.Exit")


def main():
    manager = TaskManager()
    loading = storage.load_tasks()
    for task in loading:
        TaskManag

    while True:
        menu()
        try:
            choice = int(input("Enter your choice(number): "))
        except ValueError:
            print("please enter a number")
            continue

        if choice == 1:

            title = input("Enter a title: ")

            description = input("Enter a discription: ")

            try:
                priority = int(input("Enter priority(number): "))

            except ValueError:
                print("just number try agin")
                continue
            try:
                deadline_str = input("Enter a deadline(YYYY-MM-DD: )")
                deadline = date.fromisoformat(deadline_str)

            except ValueError:
                print("date must be YYYY-MM-DD try agin")
                continue

            task = Task(title, description, priority, deadline)
            manager.add_task(task)
            print("Task added successfully.")

        elif choice == 2:
            try:

                task_id = int(input("Enter a id: "))
            except ValueError:
                print("id must be number")
                continue

            removed = manager.remove_task(task_id)

            if removed:
                print("task removed successfully.")
            else:
                print("task not found")

        elif choice == 3:
            tasks = manager.show_tasks()
            for task in tasks:
                print(task)
            if not tasks:
                print("NO tasks.")

        elif choice == 4:
            try:

                task_id = int(input("Enter a id: "))
            except ValueError:
                print("id must be number")
                continue

            search = manager.search_task(task_id)
            if search:
                print(search)
            else:
                print("task not found")

        elif choice == 0:
            print("bye")
            storage.save_tasks(manager.tasks)
            break

        else:
            print("please just Enter a number from 0 to 4")
