
# while loop to create main menu 
from add_task import add_task


while True:
    
    #creating overarching dictionary
    todo_list = []
    
    user_select = input("\nPress 1 to add task\nPress 2 to delete task\nPress 3 to view all tasks\nPress q to quit\n\n")

    # add task 
    if user_select == "1":
        todo_list.append(add_task())
       
    # delete task
    elif user_select == "2":
        todo_list = delete_task()
    
    # view all tasks
    elif user_select == "3":
        view_tasks()
    
    # quit 
    elif user_select.lower() == "q":
        break
    else:
        print("\nInvalid option. Try again...\n")
