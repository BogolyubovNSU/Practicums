def actions_on_numbers(input_file: str) -> str:
    """
    Function reads three integers from the input file,
    divides the first number by the second, and adds the third number.
    :param input_file: path to the input file
    :return: calculation result
    """
    with open (input_file, 'r', encoding='utf-8') as input_data:
        data_list = input_data.readlines()
        if len(data_list) > 3:
            return 'Oversupply of data.'
        elif len(data_list) < 3:
            return 'Lack of data.'
        else:
            numerical_data = []
            try:

                for line in data_list:
                    numerical_data.append(
                        float(line.replace('\n', '')))

                return str(
                    numerical_data[0] / numerical_data[1] + numerical_data[2])

            except ValueError:
                return 'data error'

            except ZeroDivisionError:
                return 'division by 0'


if __name__ == '__main__':
    with open ('output.txt', 'w', encoding='utf-8') as output_data:
        output_data.write(
            actions_on_numbers(input('Enter the path to the input file: ')))