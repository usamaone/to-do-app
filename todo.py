3# todo.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Practice Python")
    view_tasks()
    mark_complete(1)
    view_tasks()

def delete_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task deleted: {removed_task}")
    else:
        print("Invalid task number.")

completed_tasks = []

def mark_complete(index):
    if 1 <= index <= len(tasks):
        completed_task = tasks.pop(index - 1)
        completed_tasks.append(completed_task)
        print(f"Task marked as complete: {completed_task}")
    else:
        print("Invalid task number.")
