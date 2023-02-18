def is_valid(letter, curr_round):
    if letter.lower() in curr_round.get_already_tried_letters():
        print("You have already used this letter. Try again!")
        return False

    if len(letter) == 1:
        if letter.isalpha():
            return True
        else:
            print("Sorry, no characters except letters. Try again!")
    elif len(letter) < 1:
        print("Please enter the letter")
    else:
        print("Sorry, input size cannot be more than one letter. Try again!")

    return False
