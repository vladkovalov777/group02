from utils import (
    greet_person,
    is_even,
    reverse_string,
    calculate_average,
    add_person_to_list,
    count_vowels,
    fahrenheit_to_celsius,
)


def test_greet_person_default():
    expected = "Hello, Guest!"
    result = greet_person()
    assert result == expected, "Should greet the default guest"


def test_greet_person_with_name():
    expected = "Hello, Anna!"
    result = greet_person("Anna")
    assert result == expected, "Should greet with the given name"


def test_is_even_true():
    assert is_even(4) is True, "4 should be even"


def test_is_even_false():
    assert is_even(7) is False, "7 should be odd"


def test_reverse_string():
    assert reverse_string("hello") == "olleh", "Should reverse the string correctly"


def test_calculate_average_normal():
    numbers = [2.0, 4.0, 6.0, 8.0]
    expected = 5.0
    result = calculate_average(numbers)
    assert result == expected, "Should calculate average correctly"


def test_calculate_average_empty():
    numbers = []
    expected = 0.0
    result = calculate_average(numbers)
    assert result == expected, "Should return 0.0 for empty list"


def test_add_person_to_list():
    people = ["John", "Mary"]
    new_person = "Alice"
    new_list = add_person_to_list(people, new_person)
    assert new_list == ["John", "Mary", "Alice"], "Should add the person to the new list"
    assert people == ["John", "Mary"], "Original list should not be modified"


def test_count_vowels_english():
    text = "Hello World"
    expected = 3  # e, o, o
    result = count_vowels(text)
    assert result == expected, "Should count vowels correctly in English"


def test_count_vowels_ukrainian():
    text = "Привіт"
    expected = 2  # и, і
    result = count_vowels(text)
    assert result == expected, "Should count vowels correctly in Ukrainian"


def test_fahrenheit_to_celsius_boiling_point():
    f = 212.0
    expected = 100.0
    result = fahrenheit_to_celsius(f)
    assert round(result, 1) == expected, "212°F should be 100°C"


def test_fahrenheit_to_celsius_freezing_point():
    f = 32.0
    expected = 0.0
    result = fahrenheit_to_celsius(f)
    assert round(result, 1) == expected, "32°F should be 0°C"
