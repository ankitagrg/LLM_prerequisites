import json
import os

# File Path Setup

TASK_FILE = "data/tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    try:
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("tasks.json not found. Creating a new file...")
        tasks = []
        save_tasks(tasks)
    except json.JSONDecodeError:
        print("JSON decode error. Starting with empty tasks.")
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print(" No tasks found!")
        return
    print("\n--- To-Do List ---")
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{idx}. [{status}] {task['title']}")
    print("------------------\n")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(f"Task '{title}' added!")
    else:
        print("Task title cannot be empty!")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to remove: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' removed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as complete: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["completed"] = True
            save_tasks(tasks)
            print(f" Task '{tasks[idx - 1]['title']}' marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main Function

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do App ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task complete")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
