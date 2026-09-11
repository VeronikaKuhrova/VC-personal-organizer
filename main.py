"""A small command-line personal task organizer."""

import json
from pathlib import Path


TASKS_FILE = Path(__file__).with_name("tasks.json")
PRIORITIES = ("low", "medium", "high")


def load_tasks():
    """Return saved tasks, or an empty list when none have been saved yet."""
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read tasks.json. Starting with an empty task list.")
        return []

    return tasks if isinstance(tasks, list) else []


def save_tasks(tasks):
    """Save tasks to the local JSON file."""
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("A task title cannot be empty.")
        return

    priority = input("Priority (low, medium, high): ").strip().lower()
    if priority not in PRIORITIES:
        print("Invalid priority. Choose low, medium, or high.")
        return

    tasks.append({"title": title, "priority": priority, "completed": False})
    save_tasks(tasks)
    print("Task added.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    print("\nTasks:")
    for number, task in enumerate(tasks, start=1):
        status = "completed" if task["completed"] else "not completed"
        print(f"{number}. {task['title']} [{task['priority']}] - {status}")


def complete_task(tasks):
    if not tasks:
        print("No tasks to complete.")
        return

    list_tasks(tasks)
    choice = input("Task number to mark as completed: ").strip()

    try:
        task_number = int(choice)
        if task_number < 1:
            raise ValueError
        task = tasks[task_number - 1]
    except (ValueError, IndexError):
        print("Please enter a valid task number.")
        return

    task["completed"] = True
    save_tasks(tasks)
    print("Task marked as completed.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- PERSONAL ORGANIZER ---")
        print("1 - Add a task")
        print("2 - List tasks")
        print("3 - Mark a task as completed")
        print("0 - Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
