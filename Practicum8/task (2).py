import re


def find_max_identical(text: str) -> int:
    """
    Function. Finds the maximum number of consecutive identical characters
    in a text.

    :param text: text in which you need to find the maximum number
    of consecutive identical characters in a string

    :return: the maximum number of consecutive identical characters in a text
    """
    if not text:
        return 0
    else:
        max_similar = 0

        for similar_seq in re.finditer(r'(.)\1*', text):
            if len(similar_seq.group(0)) > max_similar:
                max_similar = len(similar_seq.group(0))

        return max_similar


if __name__ == '__main__':
    print(find_max_identical(input("Enter a string: ")))