def count_letters(word: str) -> tuple[int, int]:
    # lt := => allows to reuse the variable in the line further
    return (lt := sum(1 for x in word if x.isalpha()), len(word) - lt)


def count_letters_extended(word: str) -> tuple[int, int]:
    letter_count = 0
    for x in word:
        if x.isalpha():
            letter_count += 1
    return letter_count, len(word) - letter_count
