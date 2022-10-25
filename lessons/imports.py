"""Examples of importing in python."""


from lessons import helpers

# Alias a module / imported as another name
from lessons import helpers as hp

# Import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoint of program"""
    print(hp.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")


if __name__ == "__main__":
    main()