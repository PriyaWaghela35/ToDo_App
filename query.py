from ariadne import QueryType
from data import tasks

query = QueryType()

@query.field("task")
def resolve_task(_, info, id):
    return next((task for task in tasks if task['id'] == id), None)

@query.field("get_tasks")
def resolve_get_tasks(_, info):
    return tasks
