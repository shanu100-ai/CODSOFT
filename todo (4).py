# -------------------------------
#      TO-DO LIST APPLICATION
# -------------------------------

tasks = []  # store tasks here


def show_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Exit")
    print("================================")


def add_task():
    task = input("Enter new task: ").strip()
    if task == "":
        print("Task cannot be empty!")
    else:
        tasks.append(task)
        print("✔ Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")


def update_task():
    view_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks[num - 1] = new_task
                print("✔ Task updated!")
            else:
                print("Task cannot be empty!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"✔ Deleted: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


# ----------- MAIN LOOP -----------
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting... Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please choose between 1–5.")