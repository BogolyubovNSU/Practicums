import re


def find_max_space(text: str) -> int:
    """
    Function. Finds the maximum number of consecutive space characters
    in a text.

    :param text: a text in which you need to find the maximum number
    of consecutive space characters

    :return: the maximum number of consecutive space characters in a text
    """
    max_space = 0

    for space_seq in re.finditer(r'\s*', text):
        if len(space_seq.group()) > max_space:
            max_space = len(space_seq.group())

    return max_space


if __name__ == '__main__':
    print(find_max_space(input("Enter a string: ")))