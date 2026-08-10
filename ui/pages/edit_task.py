import customtkinter as ctk
from ui.styles import *
from validation import validate_deadline


class EditTask(ctk.CTkFrame):
    def __init__(self, parent, manager, app, task):
        super().__init__(parent, fg_color=BACKGROUND)
        self.task = task
        self.manager = manager
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            self,
            text="Edit Task",
            font=TITLE_FONT,
            text_color=TEXT
        ).grid(row=0, column=0, columnspan=2, pady=(30, 20))

        ctk.CTkLabel(
            self, text="Title", font=LABEL_FONT, text_color=TEXT
        ).grid(row=1, column=0, columnspan=2, sticky="w", padx=60, pady=(10, 2))
        self.title_entry = ctk.CTkEntry(self, width=350)
        self.title_entry.grid(
            row=2, column=0, columnspan=2, padx=60, sticky="ew")
        self.title_entry.insert(0, self.task.title)

        ctk.CTkLabel(
            self, text="Description", font=LABEL_FONT, text_color=TEXT
        ).grid(row=3, column=0, columnspan=2, sticky="w", padx=60, pady=(15, 2))
        self.description_box = ctk.CTkTextbox(self, width=350, height=120)
        self.description_box.grid(
            row=4, column=0, columnspan=2, padx=60, sticky="ew")
        self.description_box.insert("1.0", self.task.description)

        ctk.CTkLabel(
            self, text="Priority", font=LABEL_FONT, text_color=TEXT
        ).grid(row=5, column=0, sticky="w", padx=(60, 10), pady=(15, 2))
        ctk.CTkLabel(
            self, text="Deadline", font=LABEL_FONT, text_color=TEXT
        ).grid(row=5, column=1, sticky="w", padx=(10, 60), pady=(15, 2))

        self.priority_entry = ctk.CTkEntry(self, width=150)
        self.priority_entry.grid(row=6, column=0, sticky="w", padx=(60, 10))
        self.priority_entry.insert(0, str(self.task.priority))

        self.deadline_entry = ctk.CTkEntry(self, width=150)
        self.deadline_entry.grid(row=6, column=1, sticky="w", padx=(10, 60))
        self.deadline_entry.insert(
            0, str(self.task.deadline) if self.task.deadline else "")

        self.error_label = ctk.CTkLabel(
            self,
            text="",
            font=SMALL_FONT,
            text_color=ERROR_TEXT
        )
        self.error_label.grid(row=7, column=0, columnspan=2, pady=(15, 0))

        ctk.CTkButton(
            self,
            text="Save",
            fg_color=BUTTON,
            hover_color=BUTTON_HOVER,
            text_color=TEXT,
            command=self.save_changes
        ).grid(row=8, column=0, columnspan=2, pady=20)

    def show_error(self, message):
        self.error_label.configure(text=message, text_color=ERROR_TEXT)

    def clear_error(self):
        self.error_label.configure(text="")

    def save_changes(self):
        self.clear_error()

        title = self.title_entry.get().strip()
        if not title:
            self.show_error("Title cannot be empty.")
            return

        description = self.description_box.get("1.0", "end").strip()
        if not description:
            self.show_error("Description cannot be empty.")
            return

        try:
            priority = int(self.priority_entry.get())
        except ValueError:
            self.show_error("Priority must be a number.")
            return

        deadline_text = self.deadline_entry.get().strip()
        try:
            deadline = validate_deadline(deadline_text)
        except ValueError as e:
            self.show_error(str(e))
            return

        self.task.title = title
        self.task.description = description
        self.task.priority = priority
        self.task.deadline = deadline

        self.manager.update_task(self.task)
        self.app.show_tasks()
        self.destroy()
