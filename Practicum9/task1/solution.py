def convert_to_uppercase(input_file: str) -> str:
    """
    Function that converts the input data from the file to uppercase.
    :param input_file: path to the input file
    :return: converted data
    """
    with open (input_file, 'r', encoding='utf-8') as input_data:
        return input_data.read().upper()


if __name__ == '__main__':
    with open ('output.txt', 'w', encoding='utf-8') as output_data:
        output_data.write(
            convert_to_uppercase(input('Enter the path to the input file: ')))