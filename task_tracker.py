import os

def load_tasks(filename="tasks.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        file.write("\n".join(tasks))

def main():
    tasks = load_tasks()
    print("Welcome to the Task Tracker!")
    while True:
        print("\nOptions: [1] Show Tasks, [2] Add Task, [3] Delete Task, [4] Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("\nTasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        elif choice == "2":
            new_task = input("Enter new task: ").strip()
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Task added: {new_task}")
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to delete: "))
                deleted_task = tasks.pop(task_number - 1)
                save_tasks(tasks)
                print(f"Task deleted: {deleted_task}")
            except (ValueError, IndexError):
                print("Invalid input.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
