

def split_text(text, maximum_width):
    """Convert given string into list of elements (contains only whole words) with 'maximum_width'

    :param text: string passed to function
    :param maximum_width: max. width of list element
    :return: list of elements with 'maximum_width'
    """
    words = iter(text.split())
    current_set = next(words)
    final_list = []
    for word in words:
        if len(current_set) + 1 + len(word) > maximum_width:
            final_list.append(current_set)
            current_set = word
        else:
            current_set += " " + word
    final_list.append(current_set)
    return add_spaces(final_list, maximum_width)


def add_spaces(final_list, maximum_width):
    """Adds spaces between list elements words to fulfill demanded element maximum width.

    :param final_list: list of elements that not exceed maximum_width
    :param maximum_width: maximum width given by user
    :return: list of elements with spaces added'
    """
    result_list = []
    for elem in final_list[:-1]:
        while len(elem) != maximum_width:
            elem1 = elem.replace(' ', '  ', 1)
            elem = elem1
        result_list.append(elem)
    result_list.append(final_list[-1])
    return result_list


if __name__ == '__main__':
    text = "Hey there mate, it’s nice to finally meet you!"
    maximum_width = 16
    final_str = "\n".join([f'"{element}"' for element in split_text(text, maximum_width)])
    print(final_str)