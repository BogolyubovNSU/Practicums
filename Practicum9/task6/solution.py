def check_compliance(input_file: str) -> str:
    """
    Function checks whether the first line in the input file contains
    a number corresponding to the number of lines following the first line.
    :param input_file: path to the input file
    :return: YES, NO or ERROR
    """
    with open (input_file, 'r', encoding='utf-8') as input_data:
        data_list = input_data.readlines()
        try:

            if int(data_list[0].replace('\n', '')) == len(data_list) - 1:
                return 'YES'
            else:
                return 'NO'

        except ValueError:
            return 'ERROR'


if __name__ == '__main__':
    with open ('output.txt', 'w', encoding='utf-8') as output_data:
        output_data.write(
            check_compliance(input('Enter the path to the input file: ')))