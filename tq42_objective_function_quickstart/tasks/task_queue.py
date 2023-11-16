from reactivex.subject import Subject
from tq42_objective_function_quickstart.tasks.calculation import add_numbers
from tq42_objective_function_quickstart.models import Task, Result, TaskStatus
from tq42_objective_function_quickstart.config import logger


task_queue = Subject[Task]()
task_results: dict[str, Result] = {}


# noinspection PyBroadException
def calculate_and_write_to_results(task: Task) -> None:
    try:
        res = {**task.params.model_dump().copy(), "y": add_numbers(task.params.model_dump())}
        result = Result(task_id=task.task_id, result=res, status=TaskStatus.SUCCESS)
    except:
        result = Result(task_id=task.task_id, result=task.params.model_dump(), status=TaskStatus.FAILURE)
    logger.debug("Task {} produced Result {}".format(str(task.task_id), result.model_dump()))
    task_results[str(task.task_id)] = result


task_queue.subscribe(
    on_next=calculate_and_write_to_results
)
