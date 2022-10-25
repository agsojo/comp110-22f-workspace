"""EX01 - Chardle - A cute step towards Wordle!"""

__author__ = "730577804"

word: str = input("Enter a 5-character word: ")
matches: int = 0

if len(word) == 5:
    character: str = input("Enter a single character: ")
    if len(character) == 1:
        print("Searching for " + character + " in " + word)
        if word[0] == character:
            print(character + " found at index 0")
            matches = matches + 1
        if word[1] == character:
            print(character + " found at index 1")
            matches = matches + 1
        if word[2] == character:
            print(character + " found at index 2")
            matches = matches + 1
        if word[3] == character:
            print(character + " found at index 3")
            matches = matches + 1
        if word[4] == character:
            print(character + " found at index 4")
            matches = matches + 1
        if matches == 0:
            print("No instances of " + character + " found in " + word)       
        if matches > 1:
            print(str(matches) + " instances of " + character + " found in " + word)
        if matches == 1:
            print(str(matches) + " instance of " + character + " found in " + word)
    else:
        print("Error: Character must be a single letter.")
        exit()
else:
    print("Error: Word must contain 5 characters")
    exit()
