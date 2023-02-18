import random


class Round:
    MAX_NO_OF_GUESSES = 6

    def __init__(self, list_of_words):
        self._word = Round.choose_a_word_and_pop_it_from_the_list(list_of_words)
        self._incomplete_word = Round.construct_word_placeholder(self.get_the_word())
        self._already_tried_letters = []
        self._guesses_left = Round.MAX_NO_OF_GUESSES
        self._letters_in_word_and_their_indices = Round.construct_the_letter_inventory(self.get_the_word())
        self._the_round_is_won = False

    def play_a_round(self, letter):
        if not self.check_if_letter_already_tried(letter):
            if letter in self.get_letter_in_word_and_their_indices():
                self.add_letter_to_incomplete_word(letter)
                if self.get_incomplete_word() == self.get_the_word():
                    self.set_the_round_is_won()
            else:
                self.decrement_no_of_tries_left()
        else:
            print(f"You already tried: {letter}, please guess another one")

    def get_the_round_is_won(self):
        return self._the_round_is_won

    def set_the_round_is_won(self):
        self._the_round_is_won = True

    def get_guesses_left(self):
        return self._guesses_left

    def decrement_no_of_tries_left(self):
        self._guesses_left -= 1

    def get_letter_in_word_and_their_indices(self):
        return self._letters_in_word_and_their_indices

    def get_the_word(self):
        return self._word

    def get_already_tried_letters(self):
        return self._already_tried_letters

    def add_letter_to_already_tried_letters(self, letter):
        self._already_tried_letters.append(letter)

    def check_if_letter_already_tried(self, letter):
        if letter not in self.get_already_tried_letters():
            self.add_letter_to_already_tried_letters(letter)
            return False
        else:
            return True

    def get_incomplete_word(self):
        return self._incomplete_word

    def set_incomplete_word(self, word):
        self._incomplete_word = word

    def list_already_tried_letters_in_natural_language(self):
        natural_language_letters_list = ""
        for idx, char in enumerate(self.get_already_tried_letters()):
            if idx == 0:
                natural_language_letters_list += char
            else:
                natural_language_letters_list += " " + char
        return natural_language_letters_list

    def add_letter_to_incomplete_word(self, letter):
        indices = self.get_letter_in_word_and_their_indices()[letter]
        curr_word = self.get_incomplete_word()

        for index in indices:
            curr_word = curr_word[:index] + letter + curr_word[index + 1:]
        self.set_incomplete_word(curr_word)

    @classmethod
    def choose_a_word_and_pop_it_from_the_list(cls, list_of_words):
        the_chosen_one = random.choice(list_of_words)
        list_of_words.pop(list_of_words.index(the_chosen_one))
        return the_chosen_one

    @classmethod
    def construct_word_placeholder(cls, word):
        word_placeholder = ""
        char = "_"
        for letter in word:
            word_placeholder = word_placeholder + char
        return word_placeholder

    @classmethod
    def construct_the_letter_inventory(cls, word):
        letters_and_their_indices = {}
        for idx, letter in enumerate(word):
            if letter in letters_and_their_indices:
                letters_and_their_indices[letter].append(idx)
            else:
                letters_and_their_indices[letter] = [idx]

        return letters_and_their_indices
