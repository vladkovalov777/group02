from uuid import uuid4
from service.logger import logger
def is_number_bigger_than_given(candidate_number: float, threshold: float = 10) -> bool:
    """according to the task #6556565"""
    return candidate_number > threshold


def add_salt_to_list(given_list: list) -> None:
    """WARNING: list is being modified globally"""
    identifier = uuid4().hex
    print(identifier)
    logger.info("tfguyr")
    given_list.append(identifier)