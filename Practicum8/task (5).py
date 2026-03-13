def find_unique_symbol(string1: str, string2: str, string3: str) -> list[chr]:
    """
    Function. Finds characters that appear in only one of these three strings.

    :param sting1: the first string
    :param string2: the second string
    :param string3: the third string

    :return: char that appear in only one of these three lines
    """
    unique_symbol = []
    chars_s1 = {char for char in string1}
    chars_s2 = {char for char in string2}
    chars_s3 = {char for char in string3}
    common_chars12 = chars_s1.intersection(chars_s2)
    common_chars13 = chars_s1.intersection(chars_s3)
    common_chars23 = chars_s2.intersection(chars_s3)
    all_chars = chars_s1.union(chars_s2, chars_s3)

    for char in all_chars:
        if (char not in common_chars12
                and char not in common_chars13
                and char not in common_chars23):
            unique_symbol.append(char)

    return unique_symbol


if __name__ == '__main__':
    string1 = input("Enter a first string: ")
    string2 = input("Enter a second string: ")
    string3 = input("Enter a third string: ")
    print(find_unique_symbol(string1, string2, string3))