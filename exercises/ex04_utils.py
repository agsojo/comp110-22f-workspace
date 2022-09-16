"""Docstring doesn't have to mean anything all autograded!"""

__author__ = "730577804"


def all(x: list[int], y: int) -> bool:
    """Input a list and int to check if every element in list is equal to int"""
    if len(x) == 0:
        return False
    i: int = 0
    while i < len(x):
        if x[i] == y:
            i += 1
        else:
            return False
    if i == len(x):
        return True


def max(a: list[int]) -> int:
    """Input a list and its max is output"""
    if len(a) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    b = a[i]
    i += 1
    while i < len(a):
        if b <= a[i]:
            b = a[i]
        i += 1
    return b


def is_equal(moo: list[int], woof: list[int]) -> bool:
    """Compares the elements of two lists to determine if they are equal"""
    if len(moo) != len(woof):
        return False
    i: int = 0
    while i < len(moo):
        if moo[i] == woof[i]:
            i += 1
        else:
            return False
    return True