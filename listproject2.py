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
        with open("tasks.txt", "r") as file:
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
    with open("tasks.txt", "a") as file:
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
        with open("tasks.txt", "r") as file:
            tasks_list = file.readlines()
        tasks_list.pop(task_index)
        with open("tasks.txt", "w") as file:
            file.writelines(tasks_list)
        # Re-read the updated tasks.txt file into the tasks list
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        time.sleep(2)
        print(f"Your task list has been updated. Here's what's left to do:\n")
        view_tasks()
    except IndexError:
        print("\nThat task number doesn't exist. Please try again.")


tasks = []


def run_program():
    active = True
    while active == True:
        try:
            display_menu()
            menu_select = input("What would you like to do? Enter a selection:\n")
            if menu_select == "1":
                add_task()
            elif menu_select == "2":
                view_tasks()
            elif menu_select == "3":
                delete_tasks()
            elif menu_select == "4":
                active = False
        except TypeError:
            time.sleep(1)
            print("\nThat's not a valid selection. Please try again.\n")
        except ValueError:
            time.sleep(1)
            print("\nThat's not a valid selection. Please try again.\n")


import time

run_program()

print("\nGoodbye!")
