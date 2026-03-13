def find_lines(input_file: str) -> list[str]:
    """
    Function only finds lines in the input file
    that have more than 20 characters.
    :param input_file: path to the input file
    :return: found lines
    """
    result = []
    with open (input_file, 'r', encoding='utf-8') as input_data:

        for line in input_data.readlines():
            if len(line) > 20:
                result.append(line)

        return result


if __name__ == '__main__':
    with open ('output.txt', 'w', encoding='utf-8') as output_data:
        output_data.writelines(
            find_lines(input('Enter the path to the input file: ')))