import time
import os

TASKS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tasks.txt")

def display_menu():
    time.sleep(2)
    print("\n" * 5)
    print("To-do List:")
    print("1. Add a task")
    print("2. View task list")
    print("3. Delete a task")
    print("4. Quit\n")


def view_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks_list = file.readlines()
        if not tasks_list:
            time.sleep(2)
            print("\nYour task list is empty.\n")
        else:
            time.sleep(2)
            print(f"\nHere is your current task list:")
            for i, task in enumerate(tasks_list, 1):
                time.sleep(1)
                print(f"{i}. {task.strip()}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def add_task():
    new_task = input("\nWhat would you like to add to the list?\n")
    with open(TASKS_FILE, "a") as file:
        file.write(f"{new_task}\n")
    time.sleep(1)
    print(f"Task '{new_task}' has been added successfully.\n")
    view_tasks()
    print("\n")


def delete_tasks():
    view_tasks()
    try:
        choice = input("Which task number would you like to delete?\n")
        task_index = int(choice) - 1
        with open(TASKS_FILE, "r") as file:
            tasks_list = file.readlines()
        tasks_list.pop(task_index)
        with open(TASKS_FILE, "w") as file:
            file.writelines(tasks_list)
        # Re-read the updated tasks.txt file into the tasks list
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        time.sleep(2)
        print(f"Your task list has been updated. Here's what's left to do:\n")
        view_tasks()
    except IndexError:
        print("\nThat task number doesn't exist. Please try again.")