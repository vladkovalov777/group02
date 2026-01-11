from revision.functions_utils import get_ticket_price


def test_get_ticket_price_kid():
    given_age = 5
    actual_result = get_ticket_price(given_age)
    expected_result = 0.0
    assert actual_result == expected_result, "Ups"


def test_get_ticket_price_teen():
    given_age = 10
    actual_result = get_ticket_price(given_age)
    expected_result = 50.0
    assert actual_result == expected_result, "Ups"


def test_get_ticket_price_adult():
    given_age = 30
    actual_result = get_ticket_price(given_age)
    expected_result = 100.0
    assert actual_result == expected_result, "Ups"


def test_get_ticket_price_senior():
    given_age = 65
    actual_result = get_ticket_price(given_age)
    expected_result = 70.0
    assert actual_result == expected_result, "Ups"
