from task_2_1 import DigitsRangeError, combinations
import pytest


@pytest.fixture()
def sample_results():
    results = combinations("23")
    return results


def test_combination_function_result_type(sample_results):
    assert type(sample_results) == list


@pytest.mark.parametrize('symbol, expected', [("1", []), ("*", []), ("#", []), ])
def test_return_empty_list_if_given_out_of_range(symbol, expected):
    result = combinations(symbol)
    assert result == expected


@pytest.mark.parametrize('digit, expected', [
    ("2", ['a', 'b', 'c']),
    ("9", ['w', 'x', 'y', 'z']),
    ("0", ['+']),
])
def test_return_digit_mapped_letters_list(digit, expected):
    result = combinations(digit)
    assert result == expected


@pytest.mark.parametrize('digit, expected', [("234", 27), ("5432", 81), ("33", 9), ])
def test_correct_result_list_according_to_given_number(digit, expected):
    result = combinations(digit)
    assert len(result) == expected


@pytest.mark.parametrize('number', ["23", "403", "5320"])
def test_if_result_list_contains_unique_elements(number):
    results = combinations(number)
    results_set = set(results)
    assert len(results_set) == len(results)


@pytest.mark.parametrize('digit', ["123", "4*3", "5#"])
def test_error_raise_when_given_has_digits_or_signs_out_of_digits_range(digit):
    with pytest.raises(DigitsRangeError):
        combinations(digit)