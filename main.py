from task import Task
from manager import TaskManager


def menu():
    print("=====WLCOME TO MENU=====")
    print("1.Add Task")
    print("2.Remove Task")
    print("3.Show Tasks")
    print("4.Search Task")
    print("0.Exit")


def main():
    manager = TaskManager()

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

            task = Task(title, description, priority)
            manager.add_task(task)
            print("Task added successfully.")

        elif choice == 2:

            title = input("Enter a title: ")
            removed = manager.remove_task(title)

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
            title = input("Enter a title: ")
            search = manager.search_task(title)
            if search:
                print(search)
            else:
                print("task not found")

        elif choice == 0:
            print("bye")
            break

        else:
            print("please just Enter a number from 0 to 4")
