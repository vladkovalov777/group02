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


def greet_person(name: str = "Guest") -> str:
    return f"Hello, {name}!"


def is_even(number: int) -> bool:
    return number % 2 == 0


def reverse_string(text: str) -> str:
    return text[::-1]


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def add_person_to_list(people: list[str], person: str) -> list[str]:
    new_list = people.copy()
    new_list.append(person)
    return new_list


def count_vowels(text: str) -> int:
    vowels = "aeiouyAEIOUY"  # English vowels only
    return sum(1 for char in text if char in vowels)


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9