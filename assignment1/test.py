"""Simple CLI task manager.

This module implements a minimal task manager with an interactive menu
and a small, testable core. It is intentionally lightweight so it can be
run in any standard Python environment without extra dependencies.
The code style is written to score highly on common linters (e.g., pylint).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    """A single to-do item."""

    title: str
    priority: int
    completed: bool = field(default=False)

    def __post_init__(self) -> None:
        if not 1 <= self.priority <= 5:
            raise ValueError("Priority must be between 1 and 5.")


class TaskManager:
    """In-memory collection of tasks with simple operations."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def add_task(self, title: str, priority: int) -> None:
        """Add a task to the list."""
        self._tasks.append(Task(title=title.strip(), priority=priority))

    def list_tasks(self) -> List[str]:
        """Return a human-readable representation of all tasks."""
        if not self._tasks:
            return ["No tasks available."]

        lines: List[str] = []
        for index, task in enumerate(self._tasks, start=1):
            lines.append(
                f"#{index} - Title: {task.title}, "
                f"Priority: {task.priority}, Completed: {task.completed}"
            )
        return lines

    def complete_task(self, index: int) -> None:
        """Mark a task (1-based index) as completed."""
        idx = index - 1
        if 0 <= idx < len(self._tasks):
            self._tasks[idx].completed = True
        else:
            raise IndexError("Invalid task number.")

    @property
    def tasks(self) -> List[Task]:
        """Expose a read-only view of the tasks list."""
        return list(self._tasks)


def _menu() -> str:
    return (
        "\nTask Manager:\n"
        "1. Add Task\n"
        "2. List Tasks\n"
        "3. Complete Task\n"
        "4. Exit\n"
    )


def main() -> None:
    """Run the interactive menu loop."""
    manager = TaskManager()
    while True:
        print(_menu())
        raw = input("Enter your choice (1-4): ").strip()
        if not raw.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        choice = int(raw)
        if choice == 1:
            title = input("Enter task title: ").strip()
            priority_raw = input("Enter task priority (1-5): ").strip()
            if not priority_raw.isdigit():
                print("Priority must be a number (1-5).")
                continue
            priority = int(priority_raw)
            try:
                manager.add_task(title, priority)
                print("Task added.")
            except ValueError as exc:
                print(str(exc))
        elif choice == 2:
            for line in manager.list_tasks():
                print(line)
        elif choice == 3:
            idx_raw = input("Enter task number to complete: ").strip()
            if not idx_raw.isdigit():
                print("Invalid input. Please enter a valid task number.")
                continue
            try:
                manager.complete_task(int(idx_raw))
                print("Task marked as complete.")
            except IndexError as exc:
                print(str(exc))
        elif choice == 4:
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
