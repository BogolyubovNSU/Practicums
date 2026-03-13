import re


def print_not_first_repeated(sentence: str) -> str:
    """
    Function. Prints the words of a sentence that are different from the 1 word
    and do not contain any repeated letters.

    :param sentence: a sentence in which you need to print words
    that are different from the first word and do not contain repeated letters

    :return: words that are different from the first word
    and do not contain repeated letters
    """
    words = re.sub(r'[\W]', ' ', sentence).lower().split()
    result = []

    for word in words:
        all_letters = [char for char in word]
        unique_letters = set(all_letters)
        if len(all_letters) == len(unique_letters) and word != words[0]:
            result.append(word)

    return ' '.join(result)


if __name__ == '__main__':
    print(print_not_first_repeated(input("Enter a sentence: ")))