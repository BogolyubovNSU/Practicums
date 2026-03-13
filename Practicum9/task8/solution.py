def calculate_daily_average(data: list[str]) -> list[str]:
    """
    Function calculates the average daily number of steps
    for each month of the year based on the input data type of list,
    where each element represents the number of steps taken on a given day
    of the year, with the first element representing data for January 1
    and the last element representing data for December 31.
    :param data: input data
    :return: list containing the average daily number of steps
    for each month of the year
    """
    data = list(map(int, data))
    leap_year = input(
        "Is the input file for a leap year? (Don't enter anything if NO): ")
    if leap_year:
        feb_index = 31 + 29
    else:
        feb_index = 31 + 28

    return [
        str(sum(data[:31]) // 31) + '\n',
        str(sum(data[31:feb_index]) // feb_index) + '\n',
        str(sum(data[feb_index:feb_index + 31]) // 31) + '\n',
        str(sum(data[feb_index + 31:feb_index + 61]) // 30) + '\n',
        str(sum(data[feb_index + 61:feb_index + 92]) // 31) + '\n',
        str(sum(data[feb_index + 92:feb_index + 122]) // 30) + '\n',
        str(sum(data[feb_index + 122:feb_index + 153]) // 31) + '\n',
        str(sum(data[feb_index + 153:feb_index + 184]) // 31) + '\n',
        str(sum(data[feb_index + 184:feb_index + 214]) // 30) + '\n',
        str(sum(data[feb_index + 214:feb_index + 245]) // 31) + '\n',
        str(sum(data[feb_index + 245:feb_index + 275]) // 30) + '\n',
        str(sum(data[feb_index + 275:feb_index + 306]) // 31)
    ]


if __name__ == '__main__':
    input_file = input('Enter the path to the input file: ')

    with open(input_file, 'r', encoding='utf-8') as input_data:
        clean_data = []

        for line in input_data.readlines():
            clean_data.append(line.replace('\n', ''))

    with open('output.txt', 'w', encoding='utf-8') as output_data:
        output_data.writelines(calculate_daily_average(clean_data))