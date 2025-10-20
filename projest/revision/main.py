from revision.functions_utils import greet_person, \
    is_even, reverse_string, calculate_average, add_person_to_list, count_vowels, fahrenheit_to_celsius


def main():
    print(greet_person())
    print(greet_person("Alex"))

    print(is_even(10))
    print(is_even(7))

    print(reverse_string("Python"))

    numbers = [10.5, 20.0, 30.5]
    print(calculate_average(numbers))

    people = ["Alice", "Bob"]
    new_people = add_person_to_list(people, "Charlie")
    print("Original list:", people)
    print("New list:", new_people)

    print(count_vowels("Hello World"))

    print(fahrenheit_to_celsius(100))


if __name__ == "__main__":
    main()