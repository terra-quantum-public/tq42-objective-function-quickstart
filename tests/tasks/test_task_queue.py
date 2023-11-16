import uuid

from tq42_objective_function_quickstart.tasks.task_queue import task_queue
from tq42_objective_function_quickstart.models import Task


def test_queue():
    task = Task(task_id=uuid.uuid4(), params={"x1": [12]})

    def handle_task(t: Task) -> None:
        assert t.task_id == task.task_id
        assert t.params == task.params

    task_queue.subscribe(handle_task)

    task_queue.on_next(task)

