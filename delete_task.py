from view_tasks import view_tasks


def delete_task(task_list):
    while True:
        if len(task_list) > 0:
            view_tasks(task_list)
            user_input = input("\nEnter the number next to the task you want to delete\nEnter 'q' to go back to the main menu\n")
            if user_input.lower() == 'q':
                break
            elif user_input.isnumeric() and 0 < int(user_input) <= len(task_list):
                delete_flag = 0
                while delete_flag == 0:
                    delete_input = input(f"\nAre you sure you want to delete the task '{task_list[int(user_input) - 1]['title']}'?\nEnter 1 to delete\nEnter 'q' to select a different task\n")
                    if int(delete_input) == 1:
                        print(f"The task '{task_list[int(user_input) - 1]['title']}' was deleted!")
                        del task_list[int(user_input) - 1] 
                        delete_flag = 1
                    elif delete_input.lower() == 'q':
                        break
                    else: 
                        print("\nInvalid selection... try again.\n")   
            else:
                print("\nInvalid selection... try again.\n")
        else:
            input("\nYou don't have any tasks. Press Enter to go to main menu...")
            return task_list

    return task_list        
            