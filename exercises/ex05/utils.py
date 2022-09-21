"""Skeleton functions to be tested."""

__author__ = "730577804"


def only_evens(a_list: list[int]) -> list[int]:
    """Given a list of integers, a list of only the even elements will be returned."""
    i: int = 0
    even_list: list[int] = []
    while i < len(a_list):
        if a_list[i] % 2 == 0:
            even_list.append(a_list[i])
        i += 1
    return even_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Given two lists, 1 list will be made with the all first list's elements followed by the second list's elements."""
    new_list: list[int] = []
    i: int = 0
    while i < len(list_one):
        new_list[i] += list_one[i]
        i += 1
    
    i = 0
    while i <len(list_two):
        new_list[i+len(list_one)] += list_two[i]
        i += 1
    
    return new_list


def sub(any_list: list[int], start: int, end: int) -> list[int]:
    """Given a list and two ints, a list will be made with the elements between the index of the first int and the second int - 1."""
    if len(any_list) == 0 or start >= len(any_list) or end <= 0:
        return []
    
    i: int = start
    j: int = end - 1        
    subset_list: list = []
    if start < 0:
        i = 0
    if end > len(any_list):
        j = len(any_list)
    if i == j:
        subset_list.append(any_list[i])
    elif i < j:
        while i < j:
            subset_list.append(any_list[i])
            i += 1
    else:
        while j < i:
            subset_list.append(any_list[i])
            i -= 1
    return subset_list