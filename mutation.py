from ariadne import MutationType
from data import tasks

mutation = MutationType()

@mutation.field("create_task")
def resolve_create_task(_, info, id, Task, Completed):
    task = { 'id':id, 'Task': Task, 'Completed':Completed}
    tasks.append(task)
    return task

@mutation.field("update_task")
def resolve_update_task(_, info, id, Task, Completed):
    task =next((t for t in tasks if t['id'] == id),None)
    if task:
        task.update({'Task':Task, 'Completed': Completed})
    return task

@mutation.field("delete_task")
def resolve_delete_task(_, info, id):
    global tasks
    task = next((t for t in tasks if t['id'] == id),None)
    if task: 
        tasks = [t for t in tasks if t['id'] != id]
    return task
