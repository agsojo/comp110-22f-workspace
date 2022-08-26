"""EX01 - Chardle - A cute step towards Wordle!"""

__author__ = "730577804"

five_word: str = input("Enter a 5-character word: ")
one_character: str = input("Enter a single character: ")

print("Searching for " + one_character + " in " + five_word)

if five_word[0] == one_character:
    print(one_character + " found at index 0")
if five_word[1] == one_character:
    print(one_character + " found at indext 1")
if five_word[2] == one_character:
    print(one_character + " found at indext 2")
if five_word[3] == one_character:
    print(one_character + " found at indext 3")
if five_word[4] == one_character:
    print(one_character + " found at indext 4")