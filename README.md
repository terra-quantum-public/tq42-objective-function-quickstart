# Creating a TQ42 objective function

Welcome to the quick start guide for the TQ42 objective function. This guide will help you create the objective function to be passed in your parameters when running certain types of experiments on TQ42. For more, visit [tq42.com](https://tq42.com). 

## Getting started

This project is managed by [poetry](https://python-poetry.org/) so please make sure to install
this first. Afterward, installing all dependencies requires only one command:

```bash
poetry install
```

To run the application afterwards while you create the poetry environment you just need to execute:

```bash
poetry run python main.py
```

This will start up the webserver on your local machine with the port 8000.

## Testing

### Automated tests

There are a few simple test cases written with [pytest](https://docs.pytest.org/).
These can be executed simply by running:

```bash
poetry run pytest
```

### Manual tests

After starting the webserver you can make requests to this one via the URL `localhost:8000`.
To make this a little bit easier use something like [Postman](https://www.postman.com/) to create your request.

A sample flow would be the following process:

1. Execute a POST request to `localhost:8000/eval` with a body in the JSON format (choose `raw` and then type `JSON`)
    ```json
   {
      "x1": [1, 2, 0.5],
      "x2": [1, 0.5, 1],
      "x3": [1, 0.5, 0]
   }
    ```

2. The response from the first request will contain a field `task_id`. Make sure to copy this task id out.
    ```json
   {
      "task_id": "d61faaf9-21e3-4670-bc15-2585cef99153"
    }
    ```

3. Now you can query the webserver for the evaluation result by executing a POST request to `localhost:8000/task_status` containing the field `task_id`.
    ```json
   {
      "task_id": "d61faaf9-21e3-4670-bc15-2585cef99153"
   }
    ```

4. This will give you the result of the objective function run for the provided parameters.
    ```json
   {
      "task_id": "d61faaf9-21e3-4670-bc15-2585cef99153",
      "result": {
          "x1": [
              1,
              2,
              0.5
          ],
          "x2": [
              1,
              0.5,
              1
          ],
          "x3": [
              1,
              0.5,
              0
          ],
          "y": [
              3,
              3.0,
              1.5
          ]
      },
      "status": "SUCCESS"
    }
    ```


## Endpoints implementation

As our web framework we are using [FastAPI](https://fastapi.tiangolo.com/).

To make the code snippets are small and comprehensive, we are focusing on the route definition. You can look at the working example yourself in [routes.py](tq42_objective_function_quickstart/routes.py).

### Eval

This endpoint serves as the entry point for evaluating a specific set of parameters.
It creates a task to be evaluated after the user is given the `task_id` (background task).

```python
@app.post("/eval")
def read_root(body: Params, background_tasks: BackgroundTasks):
    created_task = Task(id=uuid4(), params=body)
    background_tasks.add_task(queue_up_task, created_task)
    return {"task_id": str(created_task.task_id)}
```

### Task status

This endpoint serves as the result endpoint for our created task.
It searches for a result corresponding to the provided `task_id`.
For the sake of simplicity, it returns a pending result if it cannot find anything.

```python
@app.post("/task_status")
def read_item(body: TaskStatusBody) -> Result:
    if body.task_id in task_results:
        return task_results[body.task_id]

    return Result(id=uuid.UUID(body.task_id), params={}, result=None, status=TaskStatus.PENDING)
```

## Notes

This quick start guide is intended for expressing what is necessary for an objective function to work.
Taking this example to big production loads should be executed with caution as everything is stored in memory and
can be easily lost.

If you have questions about how to adapt according to your use case, feel free to get in touch with us
at [info@terraquantum.swiss](mailto:info@terraquantum.swiss).