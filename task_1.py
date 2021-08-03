def reverse_check(user_input):
    """Checks if given is 32bit number and returns its reversed form.

    :param user_input: takes number given by user
    :return: reverse number if given is 32bit, otherwise returns 0
    """
    if int(user_input) in range(-2 ** 31, (2 ** 31) - 1):
        if int(user_input) < 0:
            return f"-{user_input[:0:-1]}"
        else:
            return user_input[::-1]
    else:
        return '0'


if __name__ == '__main__':
    user_input = input("Give the number, to check if its reversed form is 32bit: ")
    print(reverse_check(user_input))
