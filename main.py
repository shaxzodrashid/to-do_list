import flet
from flet import (
    Page, Container, Row, Column, Text, Icon, icons, Checkbox, FloatingActionButton,
    AlertDialog, TextField, ElevatedButton, IconButton, WindowDragArea, padding, Divider,
    Switch, alignment
)
import json
import os

def main(page: Page):
    # Page settings
    page.title = "To-Do"
    page.window.width = 400
    page.window.height = 700
    page.window.frameless = True
    page.window.resizable = False
    page.padding = 0
    page.spacing = 0

    # Light and dark theme color palettes
    light_palette = {
        "bgcolor": "#FFFFFF",
        "primary": "#3a7ca5",
        "secondary": "#81c3d7",
        "text": "#000000",
        "task_completed": "#AAAAAA"
    }

    dark_palette = {
        "bgcolor": "#2f6690",
        "primary": "#16425b",
        "secondary": "#3a7ca5",
        "text": "#FFFFFF",
        "task_completed": "#555555"
    }

    # Set initial theme
    current_palette = dark_palette
    page.bgcolor = current_palette["bgcolor"]

    # Function to toggle between light and dark themes
    def toggle_theme(e):
        nonlocal current_palette
        current_palette = light_palette if theme_switch.value else dark_palette
        page.bgcolor = current_palette["bgcolor"]
        title_bar.bgcolor = current_palette["primary"]
        fab.bgcolor = current_palette["primary"]
        for task_item in task_items:
            task_item.update_colors()
        page.update()

    # Custom title bar with theme switch and window control buttons
    theme_switch = Switch(value=False, on_change=toggle_theme, width=50, height=30, thumb_color="white")

    title_bar = WindowDragArea(
        content=Container(
            bgcolor=current_palette["primary"],
            padding=padding.only(left=10, right=10),
            height=40,
            content=Row(
                alignment="spaceBetween",
                vertical_alignment="center",
                controls=[
                    Row(
                        spacing=5,
                        controls=[
                            Icon(icons.CHECKLIST, color="white"),
                            Text("To-Do", color="white", weight="bold")
                        ]
                    ),
                    Row(
                        spacing=0,
                        controls=[
                            theme_switch,  # theme switch added here
                            IconButton(
                                icons.REMOVE,
                                icon_size=16,
                                icon_color="white",
                                on_click=lambda e: setattr(page.window, 'minimized', True)
                            ),
                            IconButton(
                                icons.CLOSE,
                                icon_size=16,
                                icon_color="white",
                                on_click=lambda e: page.window_close()
                            )
                        ]
                    )
                ]
            )
        )
    )

    tasks = []      # List to store task data
    task_items = [] # List to store task item objects

    # Task list UI container
    task_list = Column(spacing=0, controls=[])

    # Load tasks from JSON file or initialize default tasks
    def load_tasks():
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r", encoding="utf-8") as f:
                tasks_data = json.load(f)
                for task in tasks_data:
                    tasks.append(task)
        else:
            tasks.extend([
                {"text": "Go shopping", "due": "Due today", "completed": False},
                {"text": "Call mom", "due": "Until tomorrow", "completed": False},
                {"text": "Read a book", "due": "No due date", "completed": False},
            ])
        for task in tasks:
            add_task_item(task)

    # Save tasks to JSON file
    def save_tasks():
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)

    # Add a new task item to the UI and data list
    def add_task_item(task):
        def on_delete(task_item):
            tasks.remove(task)
            task_list.controls.remove(task_item)
            page.update()
            save_tasks()

        task_item = TaskItem(task, on_delete)
        task_items.append(task_item)
        task_list.controls.append(task_item)
        page.update()

    # Custom task item component
    class TaskItem(Container):
        def __init__(self, task, on_delete):
            super().__init__()
            self.task = task
            self.on_delete = on_delete

            self.checkbox = Checkbox(
                value=task["completed"],
                on_change=self.checkbox_changed
            )
            self.task_text = Text(
                task["text"],
                weight="bold" if not task["completed"] else "normal",
                color=current_palette["text"] if not task["completed"] else current_palette["task_completed"],
            )
            self.due_text = Text(
                task.get("due", "No due date"),
                color=current_palette["text"] if not task["completed"] else current_palette["task_completed"],
            )
            self.delete_icon = IconButton(
                icons.DELETE,
                icon_color="red",
                on_click=self.delete_clicked,
                visible=False
            )

            self.row = Row(
                controls=[
                    self.checkbox,
                    self.task_text,
                    self.due_text,
                ],
                alignment="spaceBetween",
                expand=True
            )
            self.content = self.row
            self.on_hover = self.hovered
            self.bgcolor = None
            self.padding = padding.symmetric(horizontal=10, vertical=5)
            self.opacity = 1.0 if not task["completed"] else 0.5

        # Update colors based on the theme
        def update_colors(self):
            self.task_text.color = current_palette["text"] if not self.task["completed"] else current_palette["task_completed"]
            self.due_text.color = current_palette["text"] if not self.task["completed"] else current_palette["task_completed"]
            self.update()

        # Handle task completion checkbox change
        def checkbox_changed(self, e):
            self.task["completed"] = self.checkbox.value
            self.task_text.weight = "bold" if not self.task["completed"] else "normal"
            self.task_text.color = "black" if not self.task["completed"] else "grey"
            self.due_text.color = "black" if not self.task["completed"] else "grey"
            self.opacity = 1.0 if not self.task["completed"] else 0.5
            save_tasks()
            self.update()

        # Handle hover effect for delete icon visibility
        def hovered(self, e):
            if e.data == "true":
                self.bgcolor = "#f0f0f0"
                self.due_text.visible = False
                self.delete_icon.visible = True
                self.row.controls[-1] = self.delete_icon
            else:
                self.bgcolor = None
                self.due_text.visible = True
                self.delete_icon.visible = False
                self.row.controls[-1] = self.due_text
            self.update()

        # Handle delete icon click
        def delete_clicked(self, e):
            self.on_delete(self)

    # Dialog to add a new task
    def add_task_dialog(e):
        task_text = TextField(label="Task description")
        task_due = TextField(label="Due date")

        def add_clicked(e):
            task = {
                "text": task_text.value,
                "due": task_due.value if task_due.value else "No due date",
                "completed": False
            }
            tasks.append(task)
            add_task_item(task)
            save_tasks()
            page.dialog.open = False
            page.update()

        dialog = AlertDialog(
            title=Text("Add new task"),
            content=Column([task_text, task_due], tight=True),
            actions=[
                ElevatedButton("Add", on_click=add_clicked),
                ElevatedButton("Cancel", on_click=lambda e: setattr(page.dialog, 'open', False))
            ],
            actions_alignment="end",
            on_dismiss=lambda e: None
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    # Floating action button to open the new task dialog
    fab = FloatingActionButton(
        icon=icons.ADD,
        bgcolor=current_palette["primary"],
        on_click=add_task_dialog
    )
    page.floating_action_button = fab

    # Load initial tasks and UI components
    load_tasks()

    page.add(
        Column(
            spacing=0,
            controls=[
                title_bar,
                Container(
                    padding=padding.symmetric(horizontal=10),
                    content=Column(
                        controls=[
                            Container(padding=padding.only(top=10)),
                            Row(
                                controls=[Divider(thickness=1, color=current_palette["text"]), Text("Tasks", weight="bold", color="#333333"), Divider(thickness=1, color=current_palette["text"])],
                                alignment="center",
                                vertical_alignment="center",
                            ),
                            task_list
                        ]
                    )
                )
            ]
        )
    )

flet.app(target=main)
