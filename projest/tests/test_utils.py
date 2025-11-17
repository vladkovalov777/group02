from revision.functions_utils import is_number_bigger_than_given, get_string_length_no_whitespaces, get_auto_distance


def test_is_number_bigger_than_given_1():
    given_number = 5
    result = is_number_bigger_than_given(given_number)
    expected_result = False
    assert result == expected_result


def test_get_string_length_no_whitespaces_empty_string():
    given_string = ""
    expected_result = 0
    actual_result = get_string_length_no_whitespaces(given_string)
    assert actual_result == expected_result, "Ups"
    # assert None
    # assert []
    # assert 0
    # assert False


def test_get_string_length_no_whitespaces_not_empty_string():
    given_string = "123456"
    expected_result = 6
    actual_result = get_string_length_no_whitespaces(given_string)
    assert actual_result == expected_result, "Ups"


def test_get_string_length_no_whitespaces_not_empty_string_and_spaces():
    given_string = "123  456   "
    expected_result = 6
    actual_result = get_string_length_no_whitespaces(given_string)
    assert actual_result == expected_result, "Ups"


def test_get_string_length_no_whitespaces_not_empty_string_and_spaces_2():
    given_string = "kjdsffjg dfghdfkhgkdfj dfjklhg jdfh gjkfdhgh fdjg1"
    expected_result = 45
    actual_result = get_string_length_no_whitespaces(given_string)
    assert actual_result == expected_result, "Ups"


def test_get_string_length_no_whitespaces_not_empty_string_and_spaces_3():
    given_string = (
        "kjdsffjg dfghdfkhgkdfj"
        " dfjklhg jdfh gjkfdhgh fdjg1"
    )
    expected_result = 45
    actual_result = get_string_length_no_whitespaces(given_string)
    assert actual_result == expected_result, "Ups"


def test_get_auto_distance():
    # given args
    _speed = 80
    _time = 6
    actual_result = get_auto_distance(speed=_speed, time=_time)
    # actual
    expected_result = 480
    # testing block
    assert actual_result == expected_result, "Ups"