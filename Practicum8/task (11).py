import re


def find_winner(log: str) -> str:
    """
    Function. Finds the winner in the game "Cities".

    :param log: a string consisting of words (cities) separated by spaces
    that the players called

    :return: a name of the winner
    """
    result_list = ''
    log = re.sub(r'\b(\w*?)(?:ый|[ьъйы])\b', r'\1', log)
    log_list = log.lower().split()

    for index in range(len(log_list) - 1):
        current_word = log_list[index]
        next_word = log_list[index + 1]
        if current_word[len(current_word) - 1] != next_word[0]:
            if not (index + 1) % 2:
                result_list = 'Vasya'
            else:
                result_list = 'Petya'
            break

    if not result_list:
        if not len(log_list) % 2:
            result_list = 'Vasya'
        else:
            result_list = 'Petya'
    return result_list


if __name__ == '__main__':
    print(find_winner(input('Enter the game log: ')))