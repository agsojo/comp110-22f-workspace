"""Test module for utils."""

__author__ = "730577804"

from utils import only_evens, sub, concat

def test_only_evens_empty() -> None:
    """Tests only_even function with an empty list."""
    assert only_evens([]) == []


def test_only_evens_none() -> None:
    """Tests only_even function with a list containing no even numbers."""
    assert only_evens([1,3,5,7,9]) == []


def test_only_evens_all() -> None:
    """Tests only_even function with a list containing all even numbers."""
    assert only_evens([2,4,6,8,10]) == (2,4,6,8,10)


def test_only_evens_variety() -> None:
    """Tests only_even function with a list containing a mixture of even and odd numbers."""
    assert only_evens([1,212,99,43,65,42,54]) == (212,54)


def test_sub_() -> None:
    assert sub()


def test_concat_empty() -> None:
    """Tests concat with 2 empty lists."""
    assert concat([], []) == []


def test_concat_one_empty() -> None:
    """Tests concat with one of the lists being empty and the other containing ints."""
    assert concat([], [1,2]) == [1,2]


def test_concat_both() -> None:
    """Tests concat with both lists containing ints."""
    assert concat([1,2,5], [5,2,1]) == [1,2,5,5,2,1]


def test_concat_use_both_reverse() -> None:
    """Tests concat with the reverse order of test_concat_both."""
    assert concat([5,2,1], [1,2,5]) == [5,2,1,1,2,5]