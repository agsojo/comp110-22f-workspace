"""EX01 - Chardle - A cute step towards Wordle!"""

__author__ = "730577804"

word: str = input("Enter a 5-character word: ")
MATCHES: int = 0

if len(word) == 5:
    character: str = input("Enter a single character: ")
    if len(character) == 1:
        print("Searching for " + character + " in " + word)
        if word[0] == character:
            print(character + " found at index 0")
            MATCHES = MATCHES + 1
        if word[1] == character:
            print(character + " found at index 1")
            MATCHES = MATCHES + 1
        if word[2] == character:
            print(character + " found at index 2")
            MATCHES = MATCHES + 1
        if word[3] == character:
            print(character + " found at index 3")
            MATCHES = MATCHES + 1
        if word[4] == character:
            print(character + " found at index 4")
            MATCHES = MATCHES + 1
        if MATCHES == 0:
            print("No instances of " + character + " found in " + word)
            exit()       
        if MATCHES > 1:
            print(str(MATCHES) + " instances of " + character + " found in " + word)
            exit()
        if MATCHES == 1:
            print(str(MATCHES) + " instance of " + character + " found in " + word)
            exit()
    else:
        print("Error: Character must be a single letter.")
        exit()
else:
    print("Error: Word must contain 5 characters")
    exit()
