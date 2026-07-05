import csv
from task import Task
from datetime import date
from pathlib import Path
FILE_PATH = Path(__file__).parent / "task.csv"


def save_tasks(tasks):

    with FILE_PATH.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "id",
            "title",
            "description",
            "priority",
            "status",
            "date",
            "deadline"

        ])

        for task in tasks:
            writer.writerow([
                task.id,
                task.title,
                task.description,
                task.priority,
                task.done,
                task.created_at,
                task.deadline
            ])


def load_tasks():

    if not FILE_PATH.exists():
        with FILE_PATH.open("w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "id",
                "title",
                "description",
                "priority",
                "status",
                "date",
                "deadline"
            ])

    tasks = []
    with FILE_PATH.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)

        next(reader)
        for row in reader:
            task = Task(
                title=row[1],
                description=row[2],
                priority=int(row[3]),
                deadline=date.fromisoformat(row[6])
            )
            task.id = int(row[0])
            task.done = (row[4] == "True")
            task.created_at = date.fromisoformat(row[5])

            tasks.append(task)
        return tasks
