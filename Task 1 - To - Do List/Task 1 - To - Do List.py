import json
import os

FILE_NAME = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{idx}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: ")) - 1
        tasks[num]["completed"] = True
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        tasks.pop(num)
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n-- To-Do List --")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
