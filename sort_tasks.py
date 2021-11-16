def sort_tasks(list):
    for task in range(len(list)):
        if list[task]['priority'] == 'medium':
            list.insert(0, list.pop(task))
    for task in range(len(list)):
        if list[task]['priority'] == 'high':
            list.insert(0, list.pop(task))
            
