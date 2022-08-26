"""EX01 - Chardle - A cute step towards Wordle!"""

__author__ = "730577804"

five_word: str = input("Enter a 5-character word: ")
one_character: str = input("Enter a single character: ")
matches: int = 0

print("Searching for " + one_character + " in " + five_word)

if five_word[0] == one_character:
    print(one_character + " found at index 0")
    matches = matches + 1
if five_word[1] == one_character:
    print(one_character + " found at index 1")
    matches = matches + 1
if five_word[2] == one_character:
    print(one_character + " found at index 2")
    matches = matches + 1
if five_word[3] == one_character:
    print(one_character + " found at index 3")
    matches = matches + 1
if five_word[4] == one_character:
    print(one_character + " found at index 4")
    matches = matches + 1
if matches == 0:
    print("No instances of " + one_character + " found in " + five_word)
if matches == 1:
    print(str(matches) + " instance of " + one_character + " found in " + five_word)
if matches > 1:
    print(str(matches) + " instances of " + one_character + " found in " + five_word)