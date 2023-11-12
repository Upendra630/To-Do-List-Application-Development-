# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task_description = input("Enter the task description: ")
    due_date = input("Enter the due date (optional): ")
    priority = input("Enter the priority (optional): ")
    task = {"description": task_description, "due_date": due_date, "priority": priority, "completed": False}
    tasks.append(task)
    print("Task added successfully!")

# Function to display tasks
def display_tasks():
    for idx, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{idx + 1}. Description: {task['description']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Status: {status}")

# Function to mark a task as completed
def mark_completed():
    display_tasks()
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to update a task
def update_task():
    display_tasks()
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        task = tasks[task_num]
        task["description"] = input("Enter updated description: ")
        task["due_date"] = input("Enter updated due date (optional): ")
        task["priority"] = input("Enter updated priority (optional): ")
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

# Function to remove a task
def remove_task():
    display_tasks()
    task_num = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_num < len(tasks):
        del tasks[task_num]
        print("Task removed successfully!")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":  
        add_task()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        update_task()
    elif choice == "5":
        remove_task()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")