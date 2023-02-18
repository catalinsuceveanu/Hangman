from round import Round


def print_curr_game_state(curr_round):
    print(
        f"You have {curr_round.get_guesses_left()} tries left.\n",
        f"Used letters: {curr_round.list_already_tried_letters_in_natural_language()}\n",
        f"Word: {curr_round.get_incomplete_word()}"
    )
    letter = input("Guess a letter: ")
    print("\n")
    return letter


def main():
    list_of_words = ["asccaasdfgggha", "asdfddddg", "afrgffffrg"]

    curr_round = Round(list_of_words)
    print(curr_round.get_the_word())
    print(list_of_words)

    while curr_round.get_guesses_left() > 0:
        letter = print_curr_game_state(curr_round)
        if is_valid(letter):
            curr_round.play_a_round(letter.lower())


if __name__ == '__main__':
    main()