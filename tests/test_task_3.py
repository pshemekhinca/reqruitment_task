from task_3 import split_text
import pytest
import re


@pytest.fixture()
def sample_text():
    return "Hey there mate, it’s nice to finally meet you!"


@pytest.fixture()
def max_width():
    return 12


def test_list_elements_length_does_not_exceed_max_width(sample_text, max_width):
    result = split_text(sample_text, max_width)
    for element in result:
        assert len(element) <= max_width


def test_list_elements_length_equals_max_width(sample_text, max_width):
    # Excluding last element. The task assumptions states that last line shouldn't be filled with whitespaces.
    result = split_text(sample_text, max_width)
    list_results = result[:-1]
    for element in list_results:
        assert len(element) == max_width


def test_function_return_type(sample_text, max_width):
    result = split_text(sample_text, max_width)
    assert type(result) == list
