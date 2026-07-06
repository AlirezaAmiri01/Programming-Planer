from task import Task
from manager import TaskManager
import storage
from datetime import date


def menu():
    print("\n=====WLCOME TO MENU=====\n")
    print("1.Add Task\n")
    print("2.Remove Task\n")
    print("3.Show Tasks\n")
    print("4.Search Task\n")
    print("5.Edit Task\n")
    print("6.Mark Task Done\n")
    print("7.Mark Task Pending\n")
    print("8.Sort Tasks")
    print("0.Exit\n")


def edit_menu():
    print("======WELCOME TO EDIT MENU=====\n")
    print("1.Edit Title\n")
    print("2.Edit Description\n")
    print("3.Edit Priority\n")
    print("4.Edit Deadline\n")
    print("5.Edit All\n")
    print("6.Cancel\n")


def sort_menu():
    print("=====WELCOME TO SORT MENU=====\n")
    print("1.Sort Task By Priority\n")
    print("2.Sort Task By Title\n")
    print("3.Sort Task By Created Date \n")
    print("4.Sort Task By Deadline\n")
    print("5.Cancel\n")


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
                deadline_str = input("Enter a deadline(YYYY-MM-DD): ")
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

        elif choice == 6:
            try:

                task_id = int(input("Enter a id: "))
            except ValueError:
                print("id must be number")
                continue

            done_mark = manager.mark_task_done(task_id)
            if done_mark:
                print("Task mark as done")
            else:
                print("task not found")

        elif choice == 7:
            try:

                task_id = int(input("Enter a id: "))
            except ValueError:
                print("id must be number")
                continue

            pending_mark = manager.mark_task_pending(task_id)

            if pending_mark:
                print("Task Mark as Pending ")
            else:
                print("Task not found")

        elif choice == 0:
            print("bye")
            storage.save_tasks(manager.tasks)
            break

        elif choice == 8:
            sort_menu()
            try:
                sort_choice = int(input("Enter your choice(number): "))
            except ValueError:
                print("just Enter a number")
                continue

            if sort_choice == 1:
                manager.sort_by_priority()
                print("tasks sorted by priority\n")
                for task in manager.tasks:
                    print(task)

            elif sort_choice == 2:
                manager.sort_by_title()
                print("tasks sorted by title")
                for task in manager.tasks:
                    print(task)

            elif sort_choice == 3:
                manager.sort_by_create_at()
                for task in manager.tasks:
                    print(task)

            elif sort_choice == 4:
                manager.sort_by_deadline()
                for task in manager.tasks:
                    print(task)

            elif sort_choice == 5:
                print("sort task cancled")
                continue
            else:
                print("Enter number from 1 to 5")

        else:
            print("please just Enter a number from 0 to 8")


if __name__ == "__main__":
    main()
