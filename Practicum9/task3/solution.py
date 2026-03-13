def create_word(input_file: str) -> str:
    """
    Function creates a word using the first characters of each line
    in the input file.
    :param input_file: path to the input file
    :return: created word
    """
    result = ''
    with open (input_file, 'r', encoding='utf-8') as input_data:

        for line in input_data.readlines():
            result += line[0]

        return result


if __name__ == '__main__':
    with open ('output.txt', 'w', encoding='utf-8') as output_data:
        output_data.write(
            create_word(input('Enter the path to the input file: ')))