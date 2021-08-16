import re
import itertools


class DigitsRangeError(Exception):
    """Custom exception class to describe error raised when digits are given out of the range from 2 to 9."""

    def __init__(self, given):
        super().__init__(
            f"In given number <{given}> found '1', '*', or '#'. For more than one digit numbers, only digits "
            f"from the range of 2-9 should be used!")


def combinations(given):
    """Makes all possible characters combination of given digits that are mapped to specific characters sets.

    :param given: str of given number
    :raises custom DigitsRangeError: when given number includes digits or signs out of range of 2 to 9
    :return: 'results' table with all possible characters combination
    """

    if given in ["*", "#", "1"] or len(given) == 0:
        return []
    elif re.findall(r'[ˆ1*#]', given):
        raise DigitsRangeError(given)

    digits_to_alpha = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz', 0: '+'}

    results = []
    for digit in list(given):
        results.append(list(digits_to_alpha[int(digit)]))
        final_result = ([''.join(s) for s in itertools.product(*results)])

    return final_result


if __name__ == '__main__':
    user_input = input("Enter number(s) from phone dial keyboard\n"
                       "Give numbers within range from 2 to 9: ")
    print(combinations(user_input))
