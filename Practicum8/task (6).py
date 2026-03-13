import re


def print_reverse(sentence: str) -> str:
    """
    Function. Prints the sentence in reverse word order.

    :param sentence: sentence to print.

    :return: sentence in reverse word order.
    """
    words = re.sub(r'[\W]', ' ', sentence).split()
    words.reverse()
    return " ".join(words).lower()


if __name__ == '__main__':
    print(print_reverse(input("Enter a sentence: ")))