def count_letters(word: str) -> tuple[int, int]:
    """
    Counts letters in a word

    >>> count_letters('Hello world!')
    (10, 2)
    >>> count_letters(' ')
    (0, 1)
    """
    # lt := => allows to reuse the variable in the line further
    return (lt := sum(1 for x in word if x.isalpha()), len(word) - lt)
