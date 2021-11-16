def view_tasks(task_list):
    print()
    for task in range(len(task_list)):
        print(f'{task+1} - {task_list[task]["title"]} - {task_list[task]["priority"]}')
