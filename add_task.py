def add_task():
     
    add_list = []

    while True:
        # create temporary dict
        add_task_dict = {}
        
        # main menu flag for successful task add  
        main_menu_flag = 0
        
        user_input = input("\nEnter a task, or type 'q' to go back to main menu: ")
        if user_input.lower() == "q":
            break 
        
        add_task_dict["title"] = user_input.upper()

        # setting task priority
        while main_menu_flag == 0:
            user_input = input("\nWhat is the task priority?\nPress 1 for high\nPress 2 for medium\nPress 3 for low\nPress 'q' to go back\n\n")
            
            # high priority task 
            if user_input == "1":
                print(f"\nYou entered '{add_task_dict['title']}' as your task, and made it 'high' priority. Are you sure?")
                while True:
                    user_input = input("\nPress 1 to confirm\nPress 'q' to go back\n\n")
                    if user_input == "1":
                        add_task_dict["priority"] = "high"
                        add_list.append(add_task_dict)
                        main_menu_flag = 1
                        print(f"\n'High' priority task '{add_task_dict['title']}' successfully added!\n")
                        break
                    elif user_input.lower() == "q":
                        break
                    else:
                        print("\nInvalid option. Try Again...\n")

            # medium priority task 
            elif user_input == "2":
                print(f"\nYou entered '{add_task_dict['title']}' as your task, and made it 'medium' priority. Are you sure?")
                while True:
                    user_input = input("\nPress 1 to confirm\nPress 'q' to go back\n\n")
                    if user_input == "1":
                        add_task_dict["priority"] = "medium"
                        add_list.append(add_task_dict)
                        main_menu_flag = 1
                        print(f"\n'Medium' priority task '{add_task_dict['title']}' successfully added!\n")
                        break
                    elif user_input.lower() == "q":
                        break
                    else:
                        print("\nInvalid option. Try Again...\n")
            
            # low priority task 
            elif user_input == "3":
                print(f"\nYou entered '{add_task_dict['title']}' as your task, and made it 'low' priority. Are you sure?")
                while True:
                    user_input = input("\nPress 1 to confirm\nPress 'q' to go back\n\n")
                    if user_input == "1":
                        add_task_dict["priority"] = "low"
                        add_list.append(add_task_dict)
                        main_menu_flag = 1
                        print(f"\n'Low' priority task '{add_task_dict['title']}' successfully added!\n")
                        break
                    elif user_input.lower() == "q":
                        break
                    else:
                        print("\nInvalid option. Try Again...\n")

            # go back
            elif user_input.lower() == "q":
                break
            else:
                print("\nInvalid option. Try again...\n")

    if add_list != []:
        print(f"\nAdding {len(add_list)} task(s) and organizing to-do list...\n")
        return add_list  
    else:  
        print("\nNothing to add. Returning to main menu.\n")

# add_task()


