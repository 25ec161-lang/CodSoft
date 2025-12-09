tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            num = int(input("Task number to update: "))
            tasks[num-1] = input("Enter updated task: ")
            print("Task updated.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            num = int(input("Task number to delete: "))
            tasks.pop(num-1)
            print("Task deleted.")

    elif choice == "5":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
