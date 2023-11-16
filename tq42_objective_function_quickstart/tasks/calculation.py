from itertools import zip_longest
from typing import Dict

from tq42_objective_function_quickstart.config import logger
from tq42_objective_function_quickstart.models import ValueList


def add_numbers(parameters: Dict[str, ValueList]) -> ValueList:
    """
    add_numbers adds the value for each parameter at every position together
    """
    logger.debug("calculation is getting called with parameters: {}".format(parameters))
    return [sum(val) for val in zip_longest(*parameters.values(), fillvalue=0)]
