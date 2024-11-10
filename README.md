# To-Do List Application

A sleek and modern To-Do List application built with Python and the Flet library. This app allows users to create, track, and delete tasks, with an additional feature to toggle between Dark and Light themes.

## Features

- **Custom Title Bar:** Instead of the standard OS-provided title bar, the application has a custom-made title bar that matches the overall design of the app. It includes a close button, minimize button, and a theme switch. The custom title bar can be dragged with the mouse to move the window around the screen.
- **Dark and Light Themes:** The app supports both Dark and Light themes, allowing the user to choose the appearance they prefer.
- **Task Management:** Users can add, complete, and delete tasks with ease. Completed tasks appear faded to differentiate them from active tasks.
- **Persistent Storage:** The app saves tasks in a JSON file, so all tasks are retained even after closing and reopening the app.

## Screenshots

### Light Theme
![Light Theme](./images/light-theme.png)

### Dark Theme
![Dark Theme](./images/dark-theme.png)

## Technologies Used

- **Python:** The main programming language for building the logic of the application.
- **Flet Library:** A Python library for building user interfaces that run in both desktop and web environments. It simplifies GUI development and provides cross-platform compatibility.
- **JSON:** Used for data storage, allowing tasks to be saved in a structured format, making it easy to retrieve and update task data.

### Key Components

1. **Custom Title Bar**: The standard OS title bar is replaced with a custom one that includes a draggable area, close and minimize buttons, and a theme toggle switch. This gives the app a unique look and a consistent theme.
   
2. **Task List Management**: Each task is represented as an item in a list with a checkbox for completion status, a delete button that appears on hover, and due date text. When tasks are marked as complete, they fade and the text color changes.

3. **Theme Switching**: The `toggle_theme` function allows seamless switching between Dark and Light themes, updating the background, text colors, and other UI elements to provide a cohesive look.

### Algorithms and Functionalities

- **Task Storage Algorithm**: Tasks are stored in a JSON file. When the app starts, tasks are loaded from the file, and each time a task is added, deleted, or completed, the file is updated. This ensures that all tasks persist even if the app is closed.
  
- **Color Switching Mechanism**: The app uses dictionaries to define color palettes for Dark and Light themes. The `toggle_theme` function updates the UI colors by changing the palette based on the theme switch's state.

## Advantages

- **Cross-Platform Compatibility**: Built with the Flet library, the app can run on multiple platforms (Windows, macOS, Linux) and even as a web application.
- **Modern and Customizable UI**: The custom title bar provides a more personalized user experience, and theme switching offers flexibility in appearance.
- **Persistent Task Data**: Tasks are saved locally in a JSON file, ensuring that users won’t lose their data between sessions.
  
## Possible Improvements

- **Due Date Reminders**: Implement a reminder feature that notifies users of upcoming due dates.
- **Drag and Drop Sorting**: Allow users to reorder tasks by dragging and dropping them in the desired order.
- **Task Categories**: Add the ability to create categories or tags for better organization.
- **Synchronization**: Integrate cloud-based synchronization to access tasks from multiple devices.
- **Customizable Themes**: Allow users to create and save custom themes for a more personalized experience.

## How to Run the Application

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/todo-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd todo-app
   ```
3. Install the required dependencies:
   ```bash
   pip install flet
   ```
4. Run the application:
  ```bash
  python main.py
```

## Conclusion
This To-Do List application combines functionality and aesthetics, providing an efficient tool for task management with a clean, modern interface. By using Flet and Python, it demonstrates the power of building desktop applications in a simple yet customizable way.
