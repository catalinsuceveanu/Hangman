from round import Round
from validation import is_valid


def retrieve_words():
    '''side-note on words.txt
    every word is expected to have a newline character (\n) at the end. even the last word.
    (a plain enter on most keyboards)
    words should be lower-case and no characters/spaces'''

    input_list = []
    with open('words.txt', 'r') as input:
        for line in input:
            input_list.append(line[0:-1])  # [0:-1] removes the newline character (\n)
    return input_list


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
    list_of_words = retrieve_words()
    curr_round = Round(list_of_words)

    while curr_round.get_guesses_left() > 0:
        letter = print_curr_game_state(curr_round)
        if is_valid(letter):
            curr_round.play_a_round(letter.lower())


if __name__ == '__main__':
    main()
