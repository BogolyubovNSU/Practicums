def find_lines(input_file: str) -> list[str]:
    """
    Function finds only those lines from the input file
    that start with the Latin character 'A'.
    :param input_file: path to the input file
    :return: found lines
    """
    result = []
    with open (input_file, 'r', encoding='utf-8') as input_data:

        for line in input_data.readlines():
            if line[0].lower() == 'a':
                result.append(line)

        return result


if __name__ == '__main__':
    with open ('output.txt', 'w', encoding='utf-8') as output_data:
        output_data.writelines(
            find_lines(input('Enter the path to the input file: ')))