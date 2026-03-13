def remove_hundred(input_file: str) -> list[str]:
    """
    Function removes all lines from the input file that contain the number 100
    :param input_file: path to the input file
    :return: list without rows containing the number 100
    """
    with open (input_file, 'r', encoding='utf-8') as input_data:
        result_list = input_data.readlines()

        for line in result_list:
            if line == '100' or line == '100\n':
                result_list.remove(line)

        return result_list


if __name__ == '__main__':
    with open ('output.txt', 'w', encoding='utf-8') as output_data:
        output_data.writelines(
            remove_hundred(input('Enter the path to the input file: ')))