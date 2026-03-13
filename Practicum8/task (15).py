def host_game() -> None:
    """
    Function. It helps to organize a game called "Bulls and Cows" with
    ten attempts to guess a number. The program receives a four-digit integer
    with non-repeating digits from the host. Next, the function removes
    information from the screen by displaying 25 empty lines. After that,
    the player tries to guess the hidden number. After each attempt,
    the program reports the number of "bulls" and "cows." Bulls are digits
    that match the hidden number and are located in the same positions.
    Cows are numbers that are in the target number, but in different positions.
    If the number is guessed correctly, the message "Win!" is displayed.
    If the attempts are over, the message "Loss!" is displayed.

    :return: None
    """
    try:
        hidden_number = list(int(num) for num in
                            input("Enter a natural four-digit number: "))
        print('\n' * 25)
        attempt_number = 1

        if len(hidden_number) == 4:

            while True:
                if attempt_number <= 10:
                    estimated_number = list(int(num) for num in input())
                    attempt_number += 1
                    bulls = 0
                    cows = 0

                    for num in estimated_number:
                        if num == hidden_number[estimated_number.index(num)]:
                            bulls += 1
                        elif num in hidden_number:
                            cows += 1

                    print(f'Bulls: {bulls} Cows: {cows}')

                    if bulls == 4:
                        print('Win!')
                        break
                else:
                    print('Loss!')
                    break

        else:
            print('You need to enter a natural four-digit number.')

    except ValueError: print("Invalid number. Please try again.")


if __name__ == '__main__':
    host_game()