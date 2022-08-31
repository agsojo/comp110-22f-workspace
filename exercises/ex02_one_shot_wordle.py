"""EX02 - One Shot Wordle!"""

__author__ = "730577804"

WHITE_BOX: str = "\U00002B1C"  # white box emoji
GREEN_BOX: str = "\U0001F7E9"  # green box emoji
YELLOW_BOX: str = "\U0001F7E8"  # yellow box emoji
secret_word: str = "python"  # word that player has to guess
user_guess: str = input("What is your 6-letter guess? ")  # prompt that takes user's guessed word
i: int = 0  # loop indexing variable
emoji_string: str = ""  # variable that will be used to tell the player the characters that match in their guess to the secret

while len(user_guess) != len(secret_word):  # loop that asks user to try a different word if character length of guess doesn't match the secret
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")  # prompt that asks player to try a new word if the lengths don't match
while i < len(secret_word):  # loop that compares the indices of the guessed word to the secret
    if user_guess[i] == secret_word[i]:  # checks to see if the guess and secret have a matching index
        emoji_string = emoji_string + GREEN_BOX  # indicates that the guess and secret have a matching character in the same index
    else:
        guessed_char: bool = False  # variable to keep track of whether a guessed character appears anywhere else in the secret . Set to false becaus
        j: int = 0  # loop indexing variable
        while guessed_char is not True and j < len(secret_word):  # loop to check if the character appears anywhere else in the secret
            if user_guess[i] == secret_word[j]:  # checks if the guessed character, i, appears at different indices in the secret
                guessed_char = True  # setting guessed_char to True will end the loop
            else:
                j = j + 1  # changes the index of the secret while keeping the index of the guess the same
        if guessed_char is True:  # checks if the previous loop ended because guessed_char became True or if j became too large
            emoji_string = emoji_string + YELLOW_BOX  # indicates that guessed character does appear someplace else
        else:
            emoji_string = emoji_string + WHITE_BOX  # indicates that guessed character doesn't appear anywhere else
    i = i + 1  # changes the index that is being checked over each iteration
print(emoji_string)  # the string that indicates character matches to the player
if len(user_guess) == len(secret_word):  # checks if the guess matches the secret in character length
    if user_guess == secret_word:  # checks if the guess matches the secret
        print("Woo! You got it!")  # winning message
    else:
        print("Not quite. Play again soon!")  # losing message