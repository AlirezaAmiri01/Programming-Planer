import customtkinter as ctk
from ui.styles import *
from validation import (
    validate_title,
    validate_description,
    validate_priority,
    validate_deadline,
    parse_date
)
from task import Task
from datetime import date


class AddTask(ctk.CTkFrame):
    def __init__(self, parent, manager, app):
        super().__init__(parent, fg_color=BACKGROUND)

        self.manager = manager
        self.app = app
        self.create_widgets()

    # --------------
    # widgets
    # --------------

    def create_widgets(self):
        self.title = ctk.CTkLabel(
            self,
            text="Add Task",
            font=TITLE_FONT,
            text_color=TEXT
        )
        self.title.pack(pady=(20, 10))

        # frame
        self.form = ctk.CTkFrame(
            self, fg_color=CARD, corner_radius=20)
        self.form.pack(padx=50, pady=30, fill="both", expand=True)
        self.form.grid_columnconfigure(0, weight=1)
        self.form.grid_columnconfigure(1, weight=1)
        self.form.grid_propagate(False)

        # tite
        ctk.CTkLabel(
            self.form,
            text="Title:",
            font=LABEL_FONT,
            text_color=TEXT,
        ).grid(row=0, column=0, sticky="w",  padx=(30, 10), pady=15)

        self.title_entry = ctk.CTkEntry(self.form, width=400, height=40)
        self.title_entry.grid(row=0, column=1, sticky="w",
                              padx=(5, 20), pady=10)

        # priority
        ctk.CTkLabel(
            self.form,
            text="Priority:",
            font=LABEL_FONT,
            text_color=TEXT,
        ).grid(row=1, column=0, sticky="w", padx=(30, 10), pady=15)

        self.priority_entry = ctk.CTkEntry(self.form, width=150, height=40)
        self.priority_entry.grid(
            row=1, column=1, sticky="w", padx=(5, 20), pady=10)

        # deadline
        ctk.CTkLabel(
            self.form,
            text="Deadline:",
            font=LABEL_FONT,
            text_color=TEXT,
        ).grid(row=2, column=0, sticky="w", padx=(30, 10), pady=15)

        self.deadline_entry = ctk.CTkEntry(
            self.form, placeholder_text="Example: 2026-4-8", width=250, height=40)
        self.deadline_entry.grid(
            row=2, column=1, sticky="w", padx=(5, 20), pady=10)

        # description
        ctk.CTkLabel(
            self.form,
            text="Description:",
            font=LABEL_FONT,
            text_color=TEXT,
        ).grid(row=3, column=0, sticky="w", padx=30, pady=(15, 5))

        self.description_textbox = ctk.CTkTextbox(
            self.form, width=350, height=180)
        self.description_textbox.grid(
            row=4, column=0, columnspan=2, sticky="ew", padx=30, pady=(5, 15))

        # button
        self.save_button = ctk.CTkButton(
            self.form, text="Save", width=250, height=50, command=self.save_task, fg_color=BUTTON, hover_color=BUTTON_HOVER)
        self.save_button.grid(row=5, column=0, columnspan=2, pady=30)

        # messagelabel
        self.message_label = ctk.CTkLabel(
            self.form, text="", font=LABEL_FONT, text_color=SECONDARY_TEXT)
        self.message_label.grid(row=6, column=0, columnspan=2, pady=(0, 15))

    # ---------------------
    #  save_task func
    # ---------------------

    def save_task(self):

        title = self.title_entry.get()
        description = self.description_textbox.get("1.0", "end").strip()
        priority = self.priority_entry.get()
        deadline = self.deadline_entry.get()

        title_valid = validate_title(title)
        description_valid = validate_description(description)
        priority_valid = validate_priority(priority)

        errors = []

        if not title_valid:
            errors.append("Invalid Title")

        if not description_valid:
            errors.append("Invalid description")

        if not priority_valid:
            errors.append("Invalid priority(must be number)")

        deadline_valid = None
        try:
            deadline_valid = validate_deadline(deadline)
        except ValueError as e:
            errors.append(str(e))

        if errors:
            self.message_label.configure(
                text="\n".join(errors), text_color=ERROR_TEXT)
            return

        self.message_label.configure(text="")

        priority = int(priority)

        task = Task(title, description, priority, deadline_valid)

        self.manager.add_task(task)
        self.message_label.configure(
            text="Task added successfully", text_color=SUCCESS_TEXT)

        self.title_entry.delete(0, "end")
        self.description_textbox.delete("1.0", "end")
        self.priority_entry.delete(0, "end")
        self.deadline_entry.delete(0, "end")
