"""Dictionary tests."""

__author__ = "730577804"

import pytest
from dictionary import invert, favorite_color, count


def test_invert_key_error() -> None:
    """Tests invert function to see if a key error is raised when input dictionary has two identical values."""
    with pytest.raises(KeyError):
        my_dictionary = {"x": "y", "z": "y"}
        invert(my_dictionary)


def test_invert_one() -> None:
    """Tests invert with one key-value."""
    my_dictionary = {"x": "y"}
    assert invert(my_dictionary) == {"y": "x"}


def test_invert_multi() -> None:
    """Tests invert with multiple key-values."""
    my_dictionary = {"x": "y", "z": "a", "b": "c"}
    assert invert(my_dictionary) == {"y": "x", "a": "z", "c": "b"}


def test_favorite_color_one() -> None:
    """Tests favorite color with one key-value."""
    my_dictionary = {"aidan": "blue"}
    assert favorite_color(my_dictionary) == "blue"


def test_favorite_color_multi() -> None:
    """Tests favorite color with three colors."""
    my_dictionary = {"aidan": "blue", "remy": "black", "orson": "black", "rachel": "green"}
    assert favorite_color(my_dictionary) == "black"


def test_favorite_color_tie() -> None:
    """Tests favorite color with a tie."""
    my_dictionary = {"aidan": "blue", "remy": "black"}
    assert favorite_color(my_dictionary) == "blue"


def test_count_one_value() -> None:
    """Tests count with one element."""
    my_list = ["x"]
    assert count(my_list) == {"x": 1}


def test_count_all_different() -> None:
    """Tests count with all different values."""
    my_list = ["x", "y", "z"]
    assert count(my_list) == {"x": 1, "y": 1, "z": 1}


def test_count_all_same() -> None:
    """Tests count with all values the same."""
    my_list = ["x", "x", "x"]
    assert count(my_list) == {"x": 3}


def test_count_mix() -> None:
    """Tests count with a mixture of similar and dissimilar values."""
    my_list = ["x", "x", "y", "y", "z"]
    assert count(my_list) == {"x": 2, "y": 2, "z": 1}