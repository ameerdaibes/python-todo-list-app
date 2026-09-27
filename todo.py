FILE_NAME = "tasks.txt"


def load_tasks():
    """Load tasks from the storage file."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save all tasks to the storage file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit\n")


def add_task(task):
    """Add a task if it is not empty or already stored."""
    task = task.strip()

    if not task:
        print("Task cannot be empty.\n")
        return False

    tasks = load_tasks()

    if any(existing.lower() == task.lower() for existing in tasks):
        print("Task already exists.\n")
        return False

    tasks.append(task)
    save_tasks(tasks)

    print(f"Task '{task}' added successfully.\n")
    return True


def view_tasks():
    """Display all saved tasks with numbers."""
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.\n")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()


def mark_task_completed():
    """Remove a completed task by number or by task name."""
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.\n")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    choice = input(
        "\nEnter the task number or task name to mark as complete: "
    ).strip()

    if not choice:
        print("Input cannot be empty.\n")
        return

    task_index = None

    if choice.isdigit():
        number = int(choice)
        if 1 <= number <= len(tasks):
            task_index = number - 1
    else:
        for index, task in enumerate(tasks):
            if task.lower() == choice.lower():
                task_index = index
                break

    if task_index is None:
        print(f"Task '{choice}' not found in the list.\n")
        return

    completed_task = tasks.pop(task_index)
    save_tasks(tasks)

    print(f"Task '{completed_task}' marked as complete.\n")


def get_integer(prompt, valid_choices=None, minimum=None):
    """Read and validate an integer from the user."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if valid_choices is not None and value not in valid_choices:
            print("Please enter one of the available choices.\n")
            continue

        if minimum is not None and value < minimum:
            print(f"Please enter a number greater than or equal to {minimum}.\n")
            continue

        return value


def add_tasks_menu():
    """Handle single-task and multiple-task input."""
    mode = get_integer(
        "Add a single task or multiple tasks? "
        "(1 for single, 2 for multiple): ",
        valid_choices={1, 2},
    )

    if mode == 1:
        add_task(input("Enter the task you want to add: "))
        return

    number_of_tasks = get_integer(
        "How many tasks do you want to add? ",
        minimum=1,
    )

    for index in range(1, number_of_tasks + 1):
        add_task(input(f"Enter task {index}: "))


def main():
    print("Welcome to the To-Do List App!\n")

    while True:
        menu()

        user_input = get_integer(
            "Enter your choice (1-4): ",
            valid_choices={1, 2, 3, 4},
        )

        if user_input == 1:
            add_tasks_menu()
        elif user_input == 2:
            view_tasks()
        elif user_input == 3:
            mark_task_completed()
        else:
            print("Exiting the To-Do List App. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
