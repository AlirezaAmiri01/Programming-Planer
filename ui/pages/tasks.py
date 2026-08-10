import customtkinter as ctk
from ui.styles import *
from ui.pages.CARD.task_card import TaskCard
from datetime import datetime


class Tasks(ctk.CTkFrame):
    def __init__(self, parent, manager, app):
        super().__init__(parent, fg_color=BACKGROUND)
        self.manager = manager
        self.app = app
        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="Tasks",
            font=TITLE_FONT,
            text_color=TEXT
        )
        title.pack(pady=20)

        controls_frame = ctk.CTkFrame(self, fg_color="transparent")
        controls_frame.pack(fill="x", padx=30, pady=(0, 10))

        ctk.CTkLabel(
            controls_frame,
            text="Sort:",
            font=TEXT_FONT,
            text_color=TEXT
        ).pack(side="left", padx=(0, 10))

        self.sort_menu = ctk.CTkOptionMenu(
            controls_frame,
            values=[
                "Normal",
                "Status",
                "Priority",
                "ID",
                "Deadline"
            ],
            fg_color=BUTTON,
            button_color=BUTTON,
            button_hover_color=BUTTON_HOVER,
            text_color=TEXT,
            command=self.sort_tasks
        )

        self.sort_menu.pack(side="left", padx=5)

        self.search_entry = ctk.CTkEntry(
            controls_frame,
            width=150,
            placeholder_text="Search by ID"
        )

        self.search_entry.pack(side="right", padx=5)

        ctk.CTkButton(
            controls_frame,
            text="Search",
            width=90,
            fg_color=BUTTON,
            hover_color=BUTTON_HOVER,
            text_color=TEXT,
            command=self.search_task
        ).pack(side="right")

        ctk.CTkButton(
            controls_frame,
            text="Show All",
            width=90,
            fg_color=BUTTON,
            hover_color=BUTTON_HOVER,
            text_color=TEXT,
            command=self.show_all_tasks
        ).pack(
            side="right",
            padx=5
        )

        self.error_label = ctk.CTkLabel(
            self,
            text="",
            font=SMALL_FONT,
            text_color=ERROR_TEXT
        )

        self.error_label.pack(pady=(0, 5))

        self.tasks_frame = ctk.CTkScrollableFrame(self, fg_color=BACKGROUND)

        self.tasks_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 20)
        )

    def show_error(self, message):
        self.error_label.configure(text=message)

    def clear_error(self):
        self.error_label.configure(text="")

    def render_tasks(self, tasks):

        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        for task in tasks:

            card = TaskCard(
                self.tasks_frame,
                task,
                self.manager,
                self.app
            )

            card.pack(fill="x", pady=10)

    def load_tasks(self):

        self.clear_error()

        self.render_tasks(self.manager.show_tasks())

    def sort_tasks(self, value):

        if value == "Normal":
            self.load_tasks()

        elif value == "Status":
            self.manager.sort_by_status()
            self.load_tasks()

        elif value == "Priority":
            self.manager.sort_by_priority()
            self.load_tasks()

        elif value == "ID":
            self.manager.sort_by_id()
            self.load_tasks()

        elif value == "Deadline":
            self.manager.sort_by_deadline()
            self.load_tasks()

    def search_task(self):

        self.clear_error()

        a = self.search_entry.get().strip()

        if not a:
            self.load_tasks()
            return

        try:
            task_id = int(a)

        except ValueError:

            self.show_error("ID must be a number")
            return

        task = self.manager.search_task(task_id)

        if task is None:

            self.show_error(f"Task with ID {task_id} was not found.")

            self.render_tasks([])
            return

        self.render_tasks([task])

    def show_all_tasks(self):
        self.search_entry.delete(0, "end")
        self.sort_menu.set("Normal")
        self.clear_error()
        self.render_tasks(self.manager.show_tasks())
