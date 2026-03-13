def find_triple_symbol(text: str) -> chr:
    """
    Function. Finds which character appears exactly three times in the text.

    :param text: a text in which you need to find a character
    that appears exactly three times

    :return: a symbol that appears exactly three times in the text
    """
    for index1 in range(len(text) - 1):
        counter = 1

        for index2 in range(index1 + 1, len(text)):
            if text[index1] == text[index2]:
                counter += 1

        if counter == 3:
            return text[index1]


if __name__ == '__main__':
    print(find_triple_symbol(input('Enter a text: ')))