import re


def find_ticket() -> int:
    """
    Function. Checks the ticket number, checks if it is "lucky"
    and finds its sequence number.

    :return: the serial number of the "lucky" ticket
    """
    counter = 1

    while True:
        ticket = input(f"Enter ticket number {counter}: ")
        if not len(ticket) % 2:
            first_half = ticket[:len(ticket) // 2:]
            second_half = ticket[len(ticket) // 2::]
            numbers_first = [int(match.group(0)) for match
                             in re.finditer(r'(\d)', first_half)]
            numbers_second = [int(match.group(0)) for match
                              in re.finditer(r'(\d)', second_half)]
            if sum(numbers_first) == sum(numbers_second):
                return counter
                break
            else:
                counter += 1
        else:
            counter += 1


if __name__ == '__main__':
    print(find_ticket())