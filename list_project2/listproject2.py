from app_functions.app_functions import display_menu, view_tasks, add_task, delete_tasks
import time


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


run_program()

print("\nGoodbye!")
