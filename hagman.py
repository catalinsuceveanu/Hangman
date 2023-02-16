class Round:
    MAX_NO_OF_TRIES = 6

    def __init__(self):
        self._word = "cucu"
        self._incomplete_word = Round.construct_word_placeholder(self.get_the_word())
        self._already_tried_letters = []
        self._no_of_tries_left = Round.MAX_NO_OF_TRIES

    def get_no_of_tries_left(self):
        return self._no_of_tries_left

    def decrement_no_of_tries_left(self):
        self._no_of_tries_left -= 1

    def get_the_word(self):
        return self._word

    def get_already_tried_letters(self):
        return self._already_tried_letters

    def add_letter_to_already_tried_letters(self, letter):
        self.decrement_no_of_tries_left()
        self._already_tried_letters.append(letter)

    def try_a_letter(self, letter):
        if letter not in self.get_already_tried_letters():
            self.add_letter_to_already_tried_letters(letter)
            return True
        else:
            return False

    def get_incomplete_word(self):
        return self._incomplete_word

    @classmethod
    def construct_word_placeholder(cls, word):
        word_placeholder = ""
        char = "_"
        for letter in word:
            word_placeholder = word_placeholder + char
        return word_placeholder

    def list_already_tried_letters_in_natural_language(self):
        natural_language_letters_list = ""
        for idx, char in enumerate(self.get_already_tried_letters()):
            if idx == 0:
                natural_language_letters_list += char
            else:
                natural_language_letters_list += " " + char
        return natural_language_letters_list


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
