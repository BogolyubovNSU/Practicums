import datetime


def find_more_three_days(input_info: list[str]) -> list[str]:
    """
    Function displays the numbers of the cells
    where the luggage has been stored for more than 3 days

    :param input_info: the first line of the source file contains the current
    date: the day (exactly two digits, from 01 to 31),
    followed by a period and the month (exactly two digits, from 01 to 12).
    The second line contains the number of occupied cells,
    N (at least 3 and no more than 1000). Each of the following lines has
    the following format: <cell number> <date of baggage drop-off>
    The cell number is an integer, and the date is 5 characters:
    the day (exactly two digits, from 01 to 31),
    followed by a period and the month (exactly two digits, from 01 to 12).
    The information is sorted by cell number.
    All dates belong to the same calendar year.
    Assume that February has 28 days.

    :return: cell numbers where luggage is stored for more than 3 days
    """
    current_date = input_info[0] + '.2026'
    converted_current_date = datetime.datetime.strptime(
        current_date, '%d.%m.%Y')
    input_info = input_info[2:]
    tuples_list = []
    result_list = []

    for info in input_info:
        tuples_list.append(info.split())

    for tpl in tuples_list:
        formatted_date = tpl[1] + '.2026'
        converted_formatted_date = datetime.datetime.strptime(
            formatted_date, '%d.%m.%Y')
        if (converted_current_date - converted_formatted_date).days > 3:
            result_list.append(tpl[0] + '\n')
            
    return result_list


if __name__ == '__main__':
    input_file = input('Enter the path to the input file: ')
    with open(input_file, 'r', encoding='utf-8') as input_data:
        input_data = input_data.readlines()
        clean_data = []

        for line in input_data:
            clean_data.append(line.replace('\n', ''))
        
    with open('output.txt', 'w', encoding='utf-8') as output_data:
        output_data.writelines(find_more_three_days(clean_data))