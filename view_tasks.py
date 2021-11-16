def view_tasks(task_list):
    print()
    for i in range(len(task_list)):
        print(f'{i+1} - {task_list[i]["title"]} - {task_list[i]["priority"]}')
