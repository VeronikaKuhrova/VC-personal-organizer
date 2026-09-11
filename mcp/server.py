import json
from pathlib import Path

from mcp.server import MCPServer


mcp = MCPServer("Personal Organizer")

TASKS_FILE = Path(__file__).resolve().parents[1] / "tasks.json"
VALID_PRIORITIES = {"low", "medium", "high"}


def load_tasks():
    if not TASKS_FILE.exists():
        return []

    with TASKS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)


@mcp.tool()
def list_tasks():
    """Return all tasks stored in the Personal Organizer."""
    return load_tasks()


@mcp.tool()
def add_task(title: str, priority: str = "medium"):
    """Add a new task to the Personal Organizer."""

    priority = priority.lower()

    if priority not in VALID_PRIORITIES:
        raise ValueError("Priority must be low, medium, or high.")

    tasks = load_tasks()

    task = {
        "title": title,
        "priority": priority,
        "completed": False,
    }

    tasks.append(task)
    save_tasks(tasks)

    return task


if __name__ == "__main__":
    mcp.run()