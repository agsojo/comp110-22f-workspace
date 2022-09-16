"""Recreating functions in Python."""

__author__ = "730577804"


def all(input_list: list[int], num: int) -> bool:
    """Input a list and int to check if every element in list is equal to specific int."""
    if len(input_list) == 0:
        return False  # result of an empty list
    i: int = 0
    while i < len(input_list):
        if input_list[i] == num:
            i += 1
        else:
            return False
    return True


def max(user_list: list[int]) -> int:
    """Input a list and its max is output."""
    if len(user_list) == 0:
        raise ValueError("max() arg is an empty List")  # result of an empty list
    i: int = 0
    b = user_list[i]  # variable that takes on the value of the max element of a list
    i += 1
    while i < len(a):
        if b <= a[i]:  # compares the most recent max value with the next element in the list
            b = a[i]  # b takes on the value of the compared element if it is smaller
        i += 1
    return b  # max value


def is_equal(one_list: list[int], two_list: list[int]) -> bool:
    """Compares the elements of two lists to determine if they are equal."""
    if len(one_list) != len(two_list):
        return False  # result if two lists aren't of equal length
    i: int = 0
    while i < len(one_list):
        if one_list[i] == two_list[i]:
            i += 1
        else:
            return False  # result if lists have a different element
    return True  # result if the lists are equal