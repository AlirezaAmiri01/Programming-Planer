import customtkinter as ctk
from ui.styles import *
from tkinter import messagebox
from ui.pages.dashboard import Dashboard
from ui.pages.add_task import AddTask
from manager import TaskManager
from ui.pages.tasks import Tasks
from ui.pages.edit_task import EditTask


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.manager = TaskManager()
        self.configure_window()
        self.create_layout()

    def configure_window(self):
        ctk.set_appearance_mode("Dark")
        self.title("Planer")
        self.geometry("950x850")

    def create_layout(self):
        self.create_main_frame()
        self.configure_grid()
        self.create_sidebar()
        self.create_sidebar_buttons()
        self.create_content()
        self.show_dashboard()

    def create_main_frame(self):
        self.main_frame = ctk.CTkFrame(
            self,
            fg_color=BACKGROUND,
            corner_radius=15
        )
        self.main_frame.pack(fill="both", expand=True)

    def configure_grid(self):
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=4)
        self.main_frame.grid_rowconfigure(0, weight=1)

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(
            self.main_frame,
            width=220,
            fg_color=SIDEBAR,
            corner_radius=15
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")

    def create_content(self):
        self.content = ctk.CTkFrame(
            self.main_frame, fg_color=BACKGROUND, corner_radius=15)
        self.content.grid(row=0, column=1, sticky="nsew")

    def clear_content(self):
        for widgets in self.content.winfo_children():
            widgets.destroy()

    def create_sidebar_buttons(self):
        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Add Task", self.show_add_task),
            ("Tasks", self.show_tasks),
            ("Reset", self.confirm_reset),
            ("Exit", self.destroy)
        ]
        for text, command in buttons:
            button = ctk.CTkButton(
                self.sidebar,
                text=text,
                text_color=TEXT,
                command=command,
                fg_color=BUTTON,
                hover_color=BUTTON_HOVER,
                corner_radius=15,
                height=42,
                font=TEXT_FONT
            )
            button.pack(fill="x", pady=10, padx=20)

    def show_dashboard(self):
        self.clear_content()
        dashboard = Dashboard(self.content, self.manager)
        dashboard.pack(fill="both", expand=True)

    def show_add_task(self):
        self.clear_content()
        add_task = AddTask(self.content, self.manager, self)
        add_task.pack(fill="both", expand=True)

    def show_tasks(self):
        self.clear_content()
        tasks = Tasks(self.content, self.manager, self)
        tasks.pack(fill="both", expand=True)

    def show_edit_task(self, task):
        self.clear_content()
        edit_task = EditTask(self.content, self.manager, self, task)
        edit_task.pack(fill="both", expand=True)

    def confirm_reset(self):
        confirmed = messagebox.askyesno(
            "Reset",
            "Are you sure you want to reset? This will delete all tasks and restart IDs from 1."
        )
        if confirmed:
            self.manager.reset_all_tasks()
            self.show_dashboard()
