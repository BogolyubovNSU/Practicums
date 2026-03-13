import re


def perform_arith_op(string: str) -> float:
    """

    :param string:
    :return:
    """
    string = re.sub(r"\s", "", string)

    for char in string:

        if char == '+':
            return sum([int(num) for num in string.split(char)])

        elif char == '-':
            result = [int(num) for num in string.split(char)]
            result[1] = -result[1]
            return sum(result)

        elif string[1] == '*':
            return sum([int(num) for num in string.split(char)])

        elif string[1] == '/':
            return sum([int(num) for num in string.split(char)])




if __name__ == '__main__':
    print(perform_arith_op(input()))