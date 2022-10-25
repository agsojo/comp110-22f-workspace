"""Dictionary."""

__author__ = "730577804"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given list."""
    result: dict[str, str] = {}
    for key in x:
        if x[key] in result:
            raise KeyError
        else:
            result[x[key]] = key
    return result


def favorite_color(x: dict[str, str]) -> str:
    """Given a dictionary of favorite colors, returns the most common favorite color."""
    colors: dict[str, int] = {}
    for key in x:
        if x[key] in colors:
            colors[x[key]] += 1
        else:
            colors[x[key]] = 1
    
    winner: str = ""
    winners_buddy: int = 0
    for key in colors:
        if winners_buddy == 0:
            winner = key
            winners_buddy = colors[key]
        if winners_buddy < colors[key]:
            winner = key
            winners_buddy = colors[key]
    return winner


def count(x: list[str]) -> dict[str, int]:
    """Given a list creates a dictionary with keys as values in the list and values as the number of times the value appears in the list."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in result:
            result[x[i]] += 1
        else:
            result[x[i]] = 1
        i += 1
    return result