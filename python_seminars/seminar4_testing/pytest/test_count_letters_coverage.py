import pytest
from letters_counter import count_letters_extended as counter


def test_digits():
    assert counter("123") == (0, 3)

