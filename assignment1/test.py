"""Simple CLI todo app (iteration 2)."""

from typing import Dict, List

Task = Dict[str, object]
PRIORITY_MIN = 1
PRIORITY_MAX = 5

def add_task(tasks: List[Task]) -> None:
    """Prompt user and add a task."""
    title = input("Enter task title: ").strip()
    pr_raw = input(f"Enter priority ({PRIORITY_MIN}-{PRIORITY_MAX}): ").strip()
    if pr_raw.isdigit():
        pr = int(pr_raw)
        tasks.append({"title": title, "priority": pr, "done": False})
        print("Task added.")
    else:
        print("Priority must be a number.")

def list_tasks(tasks: List[Task]) -> None:
    """Print all tasks."""
    if not tasks:
        print("No tasks.")
    else:
        for i, t in enumerate(tasks, 1):
            print(f"#{i} - {t['title']} (p={t['priority']}) done={t['done']}")

def complete_task(tasks: List[Task]) -> None:
    """Mark a task complete by 1-based index."""
    idx_raw = input("Task number to complete: ").strip()
    if not idx_raw.isdigit():
        print("Invalid number.")
        return
    i = int(idx_raw) - 1
    if 0 <= i < len(tasks):
        tasks[i]["done"] = True
        print("Done.")
    else:
        print("No such task.")

def menu() -> None:
    """Show menu."""
    print("\n1) Add  2) List  3) Complete  4) Exit")

def main() -> None:
    """Main loop."""
    tasks: List[Task] = []
    while True:
        menu()
        choice = input("Choice: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("Bye")
            break
        else:
            print("Invalid.")


if __name__ == "__main__":
    main()
