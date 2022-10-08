"""Choose your own adventure project."""

__author__ = "730577804"

from random import randint

HEART_EYES: str = "\U0001F60D"
ANXIOUS: str = "\U0001F630"
BLANK: str = "\U0001F610"
THUMBS_UP: str = "\U0001F44D"


points: int = 0
player: str = ""


def main() -> None:
    """Main function."""
    global player
    global points
    greet()

    while points < 5:
        check: bool = False
        print(f"The lizard has {5-points} health, {player}.")
        print(f"{player}, you can choose to damage the lizard with a giant mech or with experimental super powers.")
        print(f"Although, if you are not up for the task, {player}, type I'm done.")
        damage_choice: str = input(f"What is your decision, {player}: ")
        while check is False:
            if damage_choice == "giant mech":
                mech()
                check = True
            elif damage_choice == "super powers":
                points = powers(points)
                check = True
            elif damage_choice == "I'm done":
                print(f"You let Chapel Hill be destroyed, {player}. You only damaged it {points} times.")
                exit()
            else:
                damage_choice = input(f"Please type giant mech, super powers, or I'm done, {player}.: ")
    print(f"Great job{THUMBS_UP}, {player}, you've saved Chapel Hill")


def greet() -> None:
    """Greet procedure."""
    global player
    print(f"Chapel Hill is being attacked by a giant radioactive lizard{ANXIOUS}! You have to defeat it by damaging it five times!")
    player = input("What is your name?: ")


def mech() -> None:
    """Giant mech path."""
    global player
    global points

    rng: int = randint(0, 1)
    check: bool = False
    print(f"You are now the pilot of the famous Chapel Hill giant lizard-fighting giant mech, {player}.")
    robot_choice: str = input("Would you like to box with the monster or shoot missiles at it?: ")
    while check is False:
        if robot_choice == "box":
            if rng == 0:
                print(f"Sorry, {player}, the lizard whooped your ass.")
            else:
                print("The lizard cried after you stepped on its tail.")
                points += 1
            check = True
        elif robot_choice == "missiles":
            if rng == 0:
                print(f"Good job, {player}! Your aim is immaculate!")
                points += 1
            else:
                print(f"You missed{BLANK}.")
            check = True
        else:
            robot_choice = input(f"Please type box or missiles, {player}.: ")


def powers(x: int) -> int:
    """Superpowers path."""
    global player

    rng: int = randint(0, 1)
    check: bool = False
    print(f"The experimental supehero serum gave you the powers of laser vision and super strengh, {player}.")
    hero_choice: str = input(f"Would you like to use your laser vision or super strength on the monster, {player}.: ")
    while check is False:
        if hero_choice == "laser vision":
            if rng == 0:
                print("The most beautiful person you've ever seen turned your head just as you were about to laser the lizard. You hit them instead.")
            else:
                print(f"Great job staring, {player}!")
                x += 1
            check = True
        elif hero_choice == "super strength":
            if rng == 0:
                print(f"Wow, {player}, you're so strong {HEART_EYES}{HEART_EYES}{HEART_EYES}!")
                x += 1
            else:
                print("You lost an arm wrestling conteset to the lizard.")
            check = True
        else:
            hero_choice = input(f"Please type super strength or laser vision, {player}: ")
    return x


if __name__ == "__main__":
    main()