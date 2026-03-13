import re


def find_twice_words(sentence: str) -> str:
    """
    Function. Finds two identical words in a sentence.

    :param sentence: a sentence in which you need to find two identical words

    :return: a double-repeated word
    """
    words = re.sub(r'[\W]', ' ', sentence).lower().split()

    for word in words:
        temp_words = words.copy()
        temp_words.remove(word)
        if word in temp_words:
            return word
            break


if __name__ == '__main__':
    print(find_twice_words(input("Enter a sentence: ")))