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


def  say_hellow_buddy():
    return "Hellow, buddy"

def return_biggest_num_from_array(arr):
    biggest_num = arr[0]

    for elem in arr:
        if elem > biggest_num:
            biggest_num = elem
    logger.info(f"return_biggest_num_from_array:{arr=}")
    return biggest_num
arr_1 = [1,2,3,4,5,6]
a = return_biggest_num_from_array(arr_1)
print(a)

def multiply_two_nums(one,two):
    return one*two
b = multiply_two_nums(one=3, two=5)

print(b)