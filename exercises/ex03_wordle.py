"""Wordle with 6 guesses!"""

__author__ = "730577804"

WHITE_BOX: str = "\U00002B1C"  # white box emoji
GREEN_BOX: str = "\U0001F7E9"  # green box emoji
YELLOW_BOX: str = "\U0001F7E8"  # yellow box emoji

def contains_char(word_guess: str, search_char: str) -> bool:
    """Searches for search_char in word_guess"""
    assert len(search_char) == 1
    i: int = 0
    while i < len(word_guess):
        if word_guess[i] == search_char:
            return True
        else:
            i += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Returns string of emoji given two strings of equal length"""
    assert len(guess) == len(secret)
    j: int = 0
    emoji_string: str = ""
    while j < len(secret):
        if guess[j] == secret[j]:
            emoji_string += GREEN_BOX
        elif contains_char(secret, guess[j]) == True:
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        j += 1
    return emoji_string

def input_guess(guess_length: int) -> str:
    """Prompts user for a guess of a given length"""
    user_input: str = input(f"Enter a {guess_length} character word: ")
    while len(user_input) != guess_length:
        user_input = input(f"That wasn't {guess_length} chars! Try again: ")
    return user_input

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    user_win: bool = False
    k: int = 0
    while user_win is False and k < 6:
        print(f"=== Turn {k+1}/6 ===")
        user_input: str = input_guess(len(secret_word))
        print(emojified(user_input, secret_word))
        if user_input == secret_word:
            print(f"You won in {k+1}/6 turns!")
            user_win = True
        else:
            k += 1
    if k == 6:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()