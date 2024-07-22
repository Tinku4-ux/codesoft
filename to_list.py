# todo.py

tasks = []

def add_task(title, description=""):
    tasks.append({"title": title, "description": description, "completed": False})

def view_tasks():
    for index, task in enumerate(tasks, start=1):
        status = "X" if task["completed"] else " "
        print(f"{index}. [{status}] {task['title']} - {task['description']}")

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]

# Example usage:
if __name__ == "__main__":
    while True:
        print("\nTODO LIST MENU:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            add_task(title, description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task number to mark as completed: "))
            complete_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter task number to delete: "))
            delete_task(task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
