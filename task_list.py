tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncomplete = [] 
    for item in list:
        if item["completed"] == False:
            uncomplete.append(item)
    return uncomplete


## Get a list of completed tasks
def get_completed_tasks(list):
    complete = []
    for item in list:
        if item["completed"] == True:
            complete.append(item)
    return complete

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    time_taken_list = []
    for item in list:
        if item["time_taken"]>time:
            time_taken_list.append(item)
    return time_taken_list

## Find a task with a given description
def get_task_with_description(list, description):
    for item in list:
        if item["description"] == description:
            return item


# Extention (Function): 

## Get a list of tasks by status # wait for part 2
def get_tasks_by_status(list, status):
    pass

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)



