# Python To-Do List App

A command-line To-Do List application written in Python with persistent file storage, duplicate detection, input validation, and task-completion management.

## Features

- Add a single task
- Add multiple tasks in one session
- View saved tasks as a numbered list
- Mark tasks as complete by:
  - task number
  - task name
- Persistent storage using a local text file
- Case-insensitive duplicate detection
- Empty-task validation
- Safe numeric menu input
- Graceful handling when the task file does not exist

## How It Works

Tasks are stored locally in:

```text
tasks.txt
```

The file is created automatically when the first task is saved.

Each task is stored on a separate line, allowing the application to preserve tasks between program runs.

## Running the App

Requirements:

- Python 3
- No third-party packages

Run:

```bash
python3 todo.py
```

The main menu provides four options:

```text
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Exit
```

## Example

```text
Welcome to the To-Do List App!

1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Exit

Enter your choice (1-4): 1
Add a single task or multiple tasks? (1 for single, 2 for multiple): 1
Enter the task you want to add: Finish Python assignment
Task 'Finish Python assignment' added successfully.
```

## Project Structure

```text
python-todo-list-app/
├── todo.py
├── README.md
├── .gitignore
└── LICENSE
```

The runtime `tasks.txt` file is ignored by Git so personal task data is not committed accidentally.

## Improvements Made

The original version already supported file persistence, duplicate checking, task viewing, and task completion.

This cleaned version adds:

- validation for non-numeric menu input;
- rejection of empty tasks;
- consistent case-insensitive task matching;
- completion by task number or name;
- reusable file-loading and file-saving functions;
- cleaner control flow;
- a `main()` function and standard Python entry point.

## Concepts Practiced

- Python functions
- File I/O
- Lists
- Loops
- Conditionals
- Exception handling
- Input validation
- String normalization
- Persistent data storage
- Command-line application design

## What I Learned

This project strengthened my understanding of organizing a small Python application into reusable functions, validating user input, storing data persistently in files, and handling common edge cases in command-line programs.
