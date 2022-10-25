"""Wordle with 6 guesses!"""

__author__ = "730577804"

WHITE_BOX: str = "\U00002B1C"  # white box emoji
GREEN_BOX: str = "\U0001F7E9"  # green box emoji
YELLOW_BOX: str = "\U0001F7E8"  # yellow box emoji


def contains_char(search_word: str, search_char: str) -> bool:
    """Returns True if search_char is contained in search_word and False if otherwise."""
    assert len(search_char) == 1  # returns error if search_char isn't 1 character
    i: int = 0  # loop indexing variable
    while i < len(search_word):  # loops through the indices of word_guess to determine if any match the search_char
        if search_word[i] == search_char:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns string of emoji given two strings of equal length."""
    assert len(guess) == len(secret)
    j: int = 0  # loop indexing variable
    emoji_string: str = ""  # blank string that will have emojis added to it
    while j < len(secret):  # loop which compares the indices of the guess word to the secret
        if guess[j] == secret[j]:
            emoji_string += GREEN_BOX  # green box is added if the secret and the guess have a matching index
        elif contains_char(secret, guess[j]) is True:
            emoji_string += YELLOW_BOX  # a yellow box is added if the secret have a matching character, but not in the same index
        else:
            emoji_string += WHITE_BOX  # a yellow box is added if the secret doesn't contain a certain character in the guess word
        j += 1
    return emoji_string  # the complete emoji string


def input_guess(guess_length: int) -> str:
    """Prompts user for a guess of a given length and returns the user's input if it matches the given length."""
    user_input: str = input(f"Enter a {guess_length} character word: ")
    while len(user_input) != guess_length:  # loop that insists the user input a guess of proper length
        user_input = input(f"That wasn't {guess_length} chars! Try again: ")
    return user_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"  # the word that the user is trying to guess
    user_win: bool = False  # variable that acts as a flag to indicate if the user has won or not
    k: int = 0  # loop indexing variable
    while user_win is False and k < 6:  # loop that gives the user 6 turns to play
        print(f"=== Turn {k+1}/6 ===")  # tells the user what turn they are on
        user_input: str = input_guess(len(secret_word))  # uses the input_guess function to prompt the user for a guess
        print(emojified(user_input, secret_word))  # uses the emojified function to print the comparative emoji string
        if user_input == secret_word:  # if user has won
            print(f"You won in {k+1}/6 turns!")  # winning message
            user_win = True  # the variable changes after the user wins to end the loop
        else:
            k += 1
    if k == 6:
        print("X/6 - Sorry, try again tomorrow!")  # losing message


if __name__ == "__main__":
    main()