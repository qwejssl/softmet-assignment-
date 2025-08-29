# Minimal, works but not polished (few/no docstrings, weak structure)

tasks = []

def add_task():
    title = input("Enter task title: ").strip()
    pr = input("Enter priority (1-5): ").strip()
    if pr.isdigit():
        tasks.append({"title": title, "priority": int(pr), "done": False})
    else:
        print("Priority must be a number.")

def list_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, t in enumerate(tasks, 1):
            print(f"#{i} - {t['title']} (p={t['priority']}) done={t['done']}")

def complete_task():
    idx = input("Task number to complete: ").strip()
    if not idx.isdigit():
        print("Invalid number.")
        return
    i = int(idx) - 1
    if 0 <= i < len(tasks):
        tasks[i]["done"] = True
        print("Done.")
    else:
        print("No such task.")

def menu():
    print("\n1) Add  2) List  3) Complete  4) Exit")

def main():
    while True:
        menu()
        ch = input("Choice: ").strip()
        if ch == "1":
            add_task()
        elif ch == "2":
            list_tasks()
        elif ch == "3":
            complete_task()
        elif ch == "4":
            print("Bye")
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
