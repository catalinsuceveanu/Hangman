from round import Round


def print_curr_game_state(curr_round):
    print(
        f"You have {curr_round.get_no_of_tries_left()} tries left.\n",
        f"Used letters: {curr_round.list_already_tried_letters_in_natural_language()}\n",
        f"Word: {curr_round.get_incomplete_word()}"
    )
    letter = input("Guess a letter: ")
    print("\n")
    return letter


def main():
    curr_round = Round()
    while curr_round.get_no_of_tries_left() > 0:
        letter = print_curr_game_state(curr_round)
        curr_round.add_letter_to_already_tried_letters(letter)


if __name__ == '__main__':
    main()