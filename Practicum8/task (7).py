import re


def find_shortest_word(sentence: str) -> int:
    """
    Function. Finds the length of the shortest word in a sentence.

    :param sentence: a sentence in which you need to find the length
    of the shortest word

    :return: the length of the shortest word in a sentence
    """
    words = re.sub(r'[\W]', ' ', sentence).split()
    return min(len(word) for word in words)


if __name__ == '__main__':
    print(find_shortest_word(input("Enter a sentence: ")))