import customtkinter as ctk
from ui.styles import *
from datetime import date


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent, manager):
        super().__init__(parent, fg_color=BACKGROUND)

        self.manager = manager
        self.create_widgets()

    def create_widgets(self):

        ctk.CTkLabel(
            self,
            text="Dashboard",
            font=TITLE_FONT,
            text_color=TEXT
        ).pack(pady=30)

        tasks = self.manager.show_tasks()

        total_tasks = len(tasks)

        completed_tasks = len([task for task in tasks if task.done])

        pending_tasks = total_tasks - completed_tasks

        today = date.today().strftime("%Y-%m-%d")

        cards_frame = ctk.CTkFrame(self, fg_color="transparent")

        cards_frame.pack(padx=50, pady=40, fill="both", expand=True)

        cards_frame.grid_rowconfigure(0, weight=1)
        cards_frame.grid_rowconfigure(1, weight=1)
        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)

        self.create_card(cards_frame, "Total Tasks", total_tasks, 0, 0)

        self.create_card(cards_frame, "Completed", completed_tasks, 0, 1)

        self.create_card(cards_frame, "Pending", pending_tasks, 1, 0)

        self.create_card(cards_frame, "Today", today, 1, 1)

    def create_card(self, parent, title, value, row, column):

        card = ctk.CTkFrame(parent, fg_color=CARD,
                            corner_radius=15, height=150)

        card.grid(
            row=row,
            column=column,
            padx=15,
            pady=15,
            sticky="nsew"
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=SUBTITLE_FONT,
            text_color=TEXT
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            card,
            text=str(value),
            font=TITLE_FONT,
            text_color=TEXT
        ).pack()
