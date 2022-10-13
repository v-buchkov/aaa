import pytest


def count_letters(word: str) -> tuple[int, int]:
    # lt := => allows to reuse the variable in the line further
    return (lt := sum(1 for x in word if x.isalpha()), len(word) - lt)


def test_count_letters_param(faker):
    assert faker.name()
    assert faker.phone_number()
    assert faker.date()
