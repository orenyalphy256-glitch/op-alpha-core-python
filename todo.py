"""todo.py — small CLI to-do manager (add, list, remove)."""

FILENAME = "todo.txt"

def add_task(task):
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(task.strip() + "\n")

def list_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            tasks = [line.strip() for line in f if line.strip()]
            if not tasks:
                print("No tasks yet.")
                return
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
    except FileNotFoundError:
        print("No tasks yet.")

def remove_task(index):
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            tasks = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("No tasks yet.")
        return

    try:
        index = int(index) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid index.")
            return
        removed = tasks.pop(index)
        with open(FILENAME, "w", encoding="utf-8") as f:
            for t in tasks:
                f.write(t + "\n")
        print(f"Removed: {removed}")
    except ValueError:
        print("Please provide a number for the index.")

def main():
    while True:
        print("\nCommands: add, list, remove, quit")
        cmd = input("Enter command: ").strip().lower()
        if cmd == "add":
            task = input("Task: ")
            add_task(task)
            print("Added.")
        elif cmd == "list":
            list_tasks()
        elif cmd == "remove":
            idx = input("Task number to remove: ")
            remove_task(idx)
        elif cmd == "quit":
            print("Goodbye.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
