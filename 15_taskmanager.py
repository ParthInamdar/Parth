tasks = []

def show_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Done")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "status": "pending"})
    print("Task added!")

def view_tasks():
    if not tasks:
            print("No tasks available.")
            return

    print("\nYour Tasks:")
    for index, t in enumerate(tasks):
            print(f"{index+1}. {t['task']} - {t['status']}")


def delete_task():
    pass

def mark_done():
    pass

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
