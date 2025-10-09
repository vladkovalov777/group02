from utils import (
    greet_person,
    is_even,
    reverse_string,
    calculate_average,
    add_person_to_list,
    count_vowels,
    fahrenheit_to_celsius,
)
from logger_utils import logger


def main():
    # 1. Greeting
    greeting_default = greet_person()
    logger.info(f"Greeting (default): {greeting_default}")
    print(greeting_default)

    greeting_name = greet_person("Anna")
    logger.info(f"Greeting (with name): {greeting_name}")
    print(greeting_name)

    # 2. Check if numbers are even
    for number in [10, 7]:
        result = is_even(number)
        logger.info(f"is_even({number}) = {result}")
        print(f"{number} is even? {result}")

    # 3. Reverse strings
    text = "Hello World"
    reversed_text = reverse_string(text)
    logger.info(f"reverse_string('{text}') = '{reversed_text}'")
    print(f"Reversed '{text}': '{reversed_text}'")

    # 4. Calculate average
    numbers = [3.5, 7.0, 10.0]
    avg = calculate_average(numbers)
    logger.info(f"calculate_average({numbers}) = {avg}")
    print(f"Average of {numbers}: {avg}")

    # 5. Add person to list
    people = ["John", "Mary"]
    new_list = add_person_to_list(people, "Alice")
    logger.info(f"add_person_to_list({people}, 'Alice') = {new_list}")
    print(f"New list after adding Alice: {new_list}")
    print(f"Original list: {people}")

    # 6. Count vowels
    sample_text = "Hello Привіт"
    vowels_count = count_vowels(sample_text)
    logger.info(f"count_vowels('{sample_text}') = {vowels_count}")
    print(f"Number of vowels in '{sample_text}': {vowels_count}")

    # 7. Convert Fahrenheit to Celsius
    fahrenheit = 100
    celsius = fahrenheit_to_celsius(fahrenheit)
    logger.info(f"fahrenheit_to_celsius({fahrenheit}) = {celsius}")
    print(f"{fahrenheit}°F = {celsius:.2f}°C")


if __name__ == "__main__":
    main()