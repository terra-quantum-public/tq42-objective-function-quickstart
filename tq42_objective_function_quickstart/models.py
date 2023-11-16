import uuid
from enum import Enum

from pydantic import BaseModel, RootModel
from typing import Dict, List, Union

ValueList = List[Union[int, float]]

Params = RootModel[Dict[str, ValueList]]


class TaskStatusBody(BaseModel):
    task_id: str


class TaskStatus(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    PENDING = "PENDING"


class Task(BaseModel):
    """Class to keep track of a task."""
    task_id: uuid.UUID
    params: Params


class Result (BaseModel):
    """Class to keep track of a task."""
    task_id: uuid.UUID
    result: Params
    status: TaskStatus
