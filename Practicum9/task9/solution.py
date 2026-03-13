import os


def find_even_lines(input_file: str) -> list[str]:
    """
    Function reads data from the input file and returns a list containing only
    the even lines of the original file.
    :param input_file: path to the input file
    :return: list containing only the even lines of the original file
    """
    with open (input_file, 'r', encoding='utf-8') as input_data:
        result_list = input_data.readlines()

        for index in range(0, len(result_list), 2):
            result_list[index] = ''

        return result_list


if __name__ == '__main__':
    try:
        os.mkdir('simple')
    except FileExistsError:
        pass

    with open ('simple\\output.txt', 'w', encoding='utf-8') as output_data:
        output_data.writelines(
            find_even_lines(input('Enter the path to the input file: ')))