import re


def find_different_letters(text: str) -> int:
    """
    Function. Finds how many different letters there are in a text.

    :param text: a text in which you need to count different letters

    :return: the number of different letters in the text
    """
    different_letters = set()

    for match in re.finditer(r'[a-zа-яё]', text.lower()):
        different_letters.add(match.group(0))

    return len(different_letters)


if __name__ == '__main__':
    print(find_different_letters(input("Enter a text: ")))