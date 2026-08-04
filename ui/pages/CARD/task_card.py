import customtkinter as ctk
from ui.styles import *


class TaskCard(ctk.CTkFrame):
    def __init__(self, parent, task, manager, app):
        super().__init__(parent, fg_color=CARD, corner_radius=15)
        self.task = task
        self.manager = manager
        self.app = app
        self.create_widgets()

    # -----------
    # widgets
    # -----------
    def create_widgets(self):
        ctk.CTkLabel(
            self,
            text=f"Title: {self.task.title}",
            font=SUBTITLE_FONT,
            text_color=TEXT
        ).pack(anchor="w", padx=20, pady=(15, 5))

        ctk.CTkLabel(
            self,
            text=f"ID: {self.task.id}",
            font=SMALL_FONT,
            text_color=SECONDARY_TEXT
        ).pack(anchor="w", padx=20)

        ctk.CTkLabel(
            self,
            text=f"Description: {self.task.description}",
            font=TEXT_FONT,
            text_color=SECONDARY_TEXT
        ).pack(anchor="w", padx=20, pady=5)

        ctk.CTkLabel(
            self,
            text=f"Priority: {self.task.priority}",
            font=SMALL_FONT,
            text_color=TEXT
        ).pack(anchor="w", padx=20, pady=5)

        ctk.CTkLabel(
            self,
            text=f"Deadline: {self.task.deadline}",
            font=SMALL_FONT,
            text_color=TEXT
        ).pack(anchor="w", padx=20)

        self.status_label = ctk.CTkLabel(self, text="", font=SMALL_FONT)
        self.status_label.pack(anchor="w", padx=20, pady=5)

        self.done_checkbox = ctk.CTkCheckBox(
            self,
            text="Done",
            font=TEXT_FONT,
            command=self.change_status
        )
        self.done_checkbox.pack(anchor="w", padx=20, pady=10)
        if self.task.done:
            self.done_checkbox.select()
        self.update_status()

        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(anchor="e", padx=20, pady=10)

        self.edit_button = ctk.CTkButton(
            self.buttons_frame,
            text="Edit",
            width=100,
            fg_color=BUTTON,
            hover_color=BUTTON_HOVER,
            text_color=TEXT,
            command=self.edit_task
        )
        self.edit_button.pack(side="left", padx=5)

        self.delete_button = ctk.CTkButton(
            self.buttons_frame,
            text="Delete",
            width=100,
            fg_color=BUTTON,
            hover_color=BUTTON_HOVER,
            text_color=TEXT,
            command=self.delete_task
        )
        self.delete_button.pack(side="left", padx=5)

    def change_status(self):
        if self.done_checkbox.get():
            self.manager.mark_done(self.task)
        else:
            self.manager.mark_pending(self.task)
        self.update_status()

    def update_status(self):
        if self.task.done:
            self.status_label.configure(
                text="Status: Done", text_color=SUCCESS_TEXT)
        else:
            self.status_label.configure(
                text="Status: Pending", text_color=WARNING_TEXT)

    def delete_task(self):
        self.manager.delete_task(self.task)
        self.destroy()

    def edit_task(self):
        self.app.show_edit_task(self.task)
