print("===================================")
print("         TASKFLOW CONNECT")
print("===================================")

print("1. Add Task")
print("2. View Tasks")
print("3. Update Task")
print("4. Search Task")
print("5. Exit")

choice = input("Enter your choice: ")

print("You selected:", choice)
choice = input("Enter your choice: ")
choice = input("Enter your choice: ")

if choice == "1":
    print("Add Task selected")
elif choice == "2":
    print("View Tasks selected")
elif choice == "3":
    print("Update Task selected")
elif choice == "4":
    print("Search Task selected")
elif choice == "5":
    print("Exiting TaskFlow Connect...")
else:
    print("Invalid choice.")

def add_task():
    print("Add Task")

tasks = []

def add_task():
    task_name = input("Enter task name: ")
    assigned_to = input("Enter employee name: ")
    due_date = input("Enter due date: ")

    task = {
        "name": task_name,
        "assigned_to": assigned_to,
        "due_date": due_date,
        "status": "Pending"
    }

    tasks.append(task)

    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    for task in tasks:
        print("----------------------------")
        print("Task:", task["name"])
        print("Assigned To:", task["assigned_to"])
        print("Due Date:", task["due_date"])
        print("Status:", task["status"])

def update_task():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    task_name = input("Enter the task name to update: ")

    for task in tasks:
        if task["name"].lower() == task_name.lower():
            print("1. Pending")
            print("2. In Progress")
            print("3. Completed")

            choice = input("Select new status: ")

            if choice == "1":
                task["status"] = "Pending"
            elif choice == "2":
                task["status"] = "In Progress"
            elif choice == "3":
                task["status"] = "Completed"
            else:
                print("Invalid status.")
                return

            print("Task updated successfully!")
            return

    print("Task not found.")

def search_task():
    search_name = input("Enter task name to search: ")

    found = False

    for task in tasks:
        if task["name"].lower() == search_name.lower():
            print("----------------------------")
            print("Task:", task["name"])
            print("Assigned To:", task["assigned_to"])
            print("Due Date:", task["due_date"])
            print("Status:", task["status"])
            found = True

    if not found:
        print("Task not found.")

def main_menu():
    while True:
        print("\n===================================")
        print("         TASKFLOW CONNECT")
        print("===================================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Search Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            search_task()
        elif choice == "5":
            print("Thank you for using TaskFlow Connect.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
