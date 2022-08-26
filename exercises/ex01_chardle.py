"""EX01 - Chardle - A cute step towards Wordle!"""

__author__ = "730577804"

five_word: str = input("Enter a 5-character word: ")
one_character: str = input("Enter a single character: ")

print("Searching for " + five_word + " in " + one_character)

if five_word[0] == one_character:
    print