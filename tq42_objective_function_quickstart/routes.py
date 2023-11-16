import uuid

from fastapi import FastAPI, BackgroundTasks

from tq42_objective_function_quickstart.tasks.task_queue import task_queue, task_results
from tq42_objective_function_quickstart.models import Task, Result, TaskStatus, Params, TaskStatusBody

from uuid import uuid4

app = FastAPI()


def queue_up_task(task: Task) -> None:
    task_queue.on_next(task)


@app.post("/eval")
def read_root(body: Params, background_tasks: BackgroundTasks):
    created_task = Task(task_id=uuid4(), params=body)
    background_tasks.add_task(queue_up_task, created_task)
    return {"task_id": str(created_task.task_id)}


@app.post("/task_status")
def read_item(body: TaskStatusBody) -> Result:
    if body.task_id in task_results:
        return task_results[body.task_id]

    return Result(task_id=uuid.UUID(body.task_id), result={}, status=TaskStatus.PENDING)
