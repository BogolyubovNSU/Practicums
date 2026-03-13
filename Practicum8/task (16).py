def check_brackets(text: str) -> bool:
    """
    Function. Checks whether the parentheses are correctly placed in the text
    (i.e., whether there is a matching closing parenthesis to the right of each
    opening parenthesis and a matching closing parenthesis to the left of each
    closing parenthesis).

    :param text: the text to check

    :return: True or False
    """
    ballance = 0

    for char in text:
        if char == '(':
            ballance += 1
        elif char == ')':
            ballance -= 1
            if ballance < 0:
                return False

    return ballance == 0


if __name__ == '__main__':
    print(check_brackets(input('Enter a text: ')))