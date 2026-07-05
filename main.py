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
    print("5.Edit Task")
    print("0.Exit")


def edit_menu():
    print("======WELCOME TO EDIT MENU=====")
    print("1.Edit Title")
    print("2.Edit Description")
    print("3.Edit Priority")
    print("4.Edit Deadline")
    print("5.Edit All")
    print("6.Cancel")


def main():
    manager = TaskManager()
    loading = storage.load_tasks()
    for task in loading:
        manager.tasks.append(task)

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

        elif choice == 5:
            edit_menu()
            try:
                edit_choice = int(input("Enter your choice(number): "))
            except ValueError:
                print("just number from 1 to 6")
                continue

            if edit_choice == 1:
                try:
                    task_id = int(input("Enter an id for editing"))
                except ValueError:
                    print("just Enter an id(number)")
                    continue
                new_title = input("Enter a new title: ")

                edit_t = manager.edit_title(task_id, new_title)
                if edit_t:
                    print("title task edited")
                else:
                    print("not found")

            elif edit_choice == 2:
                try:
                    task_id = int(input("Enter an id for editing"))
                except ValueError:
                    print("just Enter an id(number)")
                    continue
                new_description = input("Enter a new description: ")

                edit_des = manager.edit_description(task_id, new_description)
                if edit_des:
                    print("description task edited")
                else:
                    print("not found")

            elif edit_choice == 3:
                try:
                    task_id = int(input("Enter an id for editing"))
                except ValueError:
                    print("just Enter an id(number)")
                    continue
                try:
                    new_priority = int(input("Enter a new priority: "))
                except ValueError:
                    print("just enter a number ")
                    continue

                edit_pr = manager.edit_priority(task_id, new_priority)

                if edit_pr:
                    print("priority task edited")
                else:
                    print("not found")

            elif edit_choice == 4:
                try:
                    task_id = int(input("Enter an id for editing"))
                except ValueError:
                    print("just Enter an id(number)")
                    continue

                try:
                    new_deadlinestr = input(
                        "Enter a new deadline(YYYY-MM-DD): ")
                    new_deadlineT = date.fromisoformat(new_deadlinestr)
                except ValueError:
                    print("your deadline format must be (YYY-MM-DD)")
                    continue

                edit_deadl = manager.edit_deadline(task_id, new_deadlineT)

                if edit_deadl:
                    print("deadline edited")
                else:
                    print("not found")

            elif edit_choice == 5:
                try:
                    task_id = int(input("Enter an id for editing"))
                except ValueError:
                    print("just Enter an id(number)")
                    continue

                new_title = input("Enter a new title: ")
                edit_t = manager.edit_title(task_id, new_title)

                new_description = input("Enter a new description: ")
                edit_des = manager.edit_description(task_id, new_description)

                try:
                    new_priority = int(input("Enter a new priority: "))
                except ValueError:
                    print("just enter a number ")
                    continue

                edit_pr = manager.edit_priority(task_id, new_priority)

                try:
                    new_deadlinestr = input(
                        "Enter a new deadline(YYYY-MM-DD): ")
                    new_deadlineT = date.fromisoformat(new_deadlinestr)
                except ValueError:
                    print("your deadline format must be (YYY-MM-DD)")
                    continue

                edit_deadl = manager.edit_deadline(task_id, new_deadlineT)

                if edit_t and edit_des and edit_pr and edit_deadl:
                    print("task edited")
                else:
                    print("task not found")

            elif edit_choice == 6:
                print("editing task cancled")
                continue
            else:
                print("just a number from 1 to 6 ")

        else:
            print("please just Enter a number from 0 to 5")


if __name__ == "__main__":
    main()
