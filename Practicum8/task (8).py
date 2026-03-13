import re


def print_ascending_order(sentence: str) -> str:
    """
    Function. It prints all the words in the sentence in ascending order
    of their lengths.

    :param sentence: a sentence in which you need to print all the words
    in ascending order of length

    :return: a sentence in which all the words are printed
    in ascending order of length
    """
    words = re.sub(r'[\W]', ' ', sentence).lower().split()
    flag = True

    while flag:

        for index in range(len(words) - 1):
            if len(words[index]) >= len(words[index + 1]):
                flag = False
            else:
                flag = True
                break

        for index in range(len(words) - 1):
            if len(words[index]) < len(words[index + 1]):
                    words[index], words[index + 1] = words[index + 1], words[index]


    return " ".join(words)


if __name__ == '__main__':
    print(print_ascending_order(input("Enter a sentence: ")))