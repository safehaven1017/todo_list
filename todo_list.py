from add_task import add_task
from delete_task import delete_task
from view_tasks import view_tasks
from sort_tasks import sort_tasks

#creating overarching dictionary
todo_list = []

# while loop to create main menu 
while True:
    
    user_select = input("\nPress 1 to add task\nPress 2 to delete task\nPress 3 to view all tasks\nPress q to quit\n\n")

    # add task 
    if user_select == "1":
        todo_list = todo_list + add_task()
        sort_tasks(todo_list)

    # delete task
    elif user_select == "2":
        if len(todo_list) > 0:
            todo_list = delete_task(todo_list)
        else:
            print("\nYou must add a task before you can delete any.\n")
    
    # view all tasks
    elif user_select == "3":
        if len(todo_list) > 0:
            view_tasks(todo_list)
        else:
            print("\nYou don't have any tasks.\n")
        
    # quit 
    elif user_select.lower() == "q":
        break
    else:
        print("\nInvalid option. Try again...\n")
