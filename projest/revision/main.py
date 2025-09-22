from revision.functions_utils import is_number_bigger_than_given, add_salt_to_list, say_hellow_buddy, \
    return_biggest_num_from_array, multiply_two_nums


def main():
    result = is_number_bigger_than_given(candidate_number=5)
    print(result)
    result = is_number_bigger_than_given(candidate_number=66, threshold=1)
    print(result)


    given_list = []
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    print(given_list)
    print(say_hellow_buddy())
    arr_1 = [1, 2, 3, 4, 5, 6, 20]
    print(return_biggest_num_from_array(arr_1))
    num_one = 4
    num_two = 6
    print(multiply_two_nums(num_one, num_two))


if __name__ == "__main__":
    main()