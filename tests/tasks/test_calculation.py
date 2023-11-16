import pytest

from tq42_objective_function_quickstart.tasks.calculation import add_numbers


def test_add_numbers_empty():
    assert [] == add_numbers({})


def test_add_numbers():
    assert [2] == add_numbers({"x1": [1], "x2": [1]})
    assert [4, 4] == add_numbers({"x1": [1, 0], "x2": [1, 2], "x3": [1, 7], "x4": [1, -5]})


def test_add_numbers_different_types():
    assert [1.5] == add_numbers({"x1": [1], "x2": [0.5]})
    assert [4, 3.5] == add_numbers({"x1": [1, 1.5], "x2": [1, 0], "x3": [1, 1], "x4": [1, 1]})


def test_add_numbers_different_lengths():
    assert [2, 1, 1] == add_numbers({"x1": [1], "x2": [1, 1, 1], "x3": [0, 0]})
    assert [2, 1, 1] == add_numbers({"x1": [1, 1, 1], "x2": [1], "x3": []})
    assert [2, 1, 1] == add_numbers({"x1": [1], "x2": [1, 1, 1], "x3": [0, 0]})


def test_add_numbers_wrong_input():
    with pytest.raises(Exception):
        add_numbers({"x1": [0, "test"]})
        add_numbers({"x1": [0, 11], "x2": [0, "test"]})
        # noinspection PyTypeChecker
        add_numbers({1: [0, 11]})
