from uuid import uuid4
from service.logger import logger
def is_number_bigger_than_given(candidate_number: float, threshold: float = 10) -> bool:
    """according to the task #6556565"""
    return candidate_number > threshold





def greet_person(name: str = "Guest") -> str:
    """Returns a greeting in the format: 'Hello, <name>!'."""
    return f"Hello, {name}!"


def is_even(number: int) -> bool:
    """Returns True if the number is even, otherwise False."""
    return number % 2 == 0


def reverse_string(text: str) -> str:
    """Returns the string in reverse order."""
    return text[::-1]


def calculate_average(numbers: list[float]) -> float:
    """Calculates and returns the average of the numbers in the list."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def add_person_to_list(people: list[str], person: str) -> list[str]:
    """Adds a person to the end of the list and returns a new list (original list is not modified)."""
    new_list = people.copy()
    new_list.append(person)
    return new_list


def count_vowels(text: str) -> int:
    """Returns the number of vowels in a string (both English and Ukrainian vowels)."""
    vowels = set("aeiouyаеєиіїоуюяAEIOUYАЕЄИІЇОУЮЯ")
    return sum(1 for ch in text if ch in vowels)


def fahrenheit_to_celsius(f: float) -> float:
    """Converts temperature from Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9