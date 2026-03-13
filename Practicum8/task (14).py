def host_game() -> None:
    """
    Function. It helps to host the television game "Field of Miracles".
    Asks the host for a hint and the word to be guessed.
    Next, the function removes the information from the screen by displaying 25
    blank lines. After that, the hint and the word are displayed,
    with the letters replaced by "*". The player has ten attempts to
    guess the word by letter. After each attempt, the word is displayed with
    the unguessed letters replaced by "*". The guessed letters are displayed in
    their corresponding positions. Each attempt is accompanied by the question
    "Letter or word (0 - letter, 1 - word)?". If the word is guessed correctly,
    the message "Win!" is displayed. If the word is guessed incorrectly
    or the attempts are exhausted, the message "Loss!" is displayed.

    :return: None
    """
    hint = input("Enter a hint: ")
    hidden_word = (input('Enter the hidden word: ')).lower()
    closed_word = '*' * len(hidden_word)
    print('\n' * 25)
    print(hint)
    attempt_number = 1

    while True:
        if closed_word == hidden_word:
            print('\nWin!')
            break
        elif attempt_number > 10:
            print('\nLoss!')
            break
        else:
            print(closed_word)
            response_settings = input("\nLetter or word"
                                      "(0 - letter, 1 - word)? ")
            if response_settings == '1':
                whole_word = input().lower()
                if whole_word == hidden_word:
                    print('\nWin!')
                else:
                    print('\nLoss!')
                break
            elif response_settings == '0':
                letter = input().lower()

                for char in hidden_word:
                    if char == letter:
                        temp_closed_word = list(closed_word)
                        temp_closed_word[hidden_word.index(char)] = letter
                        closed_word = ''.join(temp_closed_word)

                attempt_number += 1

            else:
                print('\nTo choose how to answer, enter 0 or 1.')


if __name__ == '__main__':
    host_game()