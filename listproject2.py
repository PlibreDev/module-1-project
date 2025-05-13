def display_menu():
    print("\nTo-do List:")
    print("1. Add a task")
    print("2. View task list")
    print("3. Delete a task")
    print("4. Quit\n")

def view_tasks():
    try:
        if not tasks:
            print("\nYour task list is empty.\n")
        else:
            print(f"\nHere is your current task list:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
def add_task():
    new_task = input("\nWhat would you like to add to the list?\n")
    tasks.append(new_task)
    print(f"Task '{new_task}' has been added successfully.\n")
    view_tasks()
    print() #used just to create a new line after the task list is printed

def delete_tasks():
    view_tasks()
    try:
        choice = input("Which task number would you like to delete?\n")
        tasks.pop(int(choice)- 1)
        print(f"Your task list has been updated. Here's what's left to do:\n")
        view_tasks()    
    except IndexError:
            print("\nThat task number doesn't exist. Please try again.") 

tasks = []
def run_program():
    active = True
    while active == True:
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
        
        
run_program()   