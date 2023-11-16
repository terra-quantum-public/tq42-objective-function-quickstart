import uvicorn

from tq42_objective_function_quickstart.config import logger
from tq42_objective_function_quickstart.routes import app

if __name__ == "__main__":
    logger.info("Welcome to the tq42 objective function quickstart sample")
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8000,
        log_level='info',
        loop='asyncio'
    )


