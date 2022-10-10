def count_letters(word: str) -> tuple[int, int]:
    # lt := => allows to reuse the variable in the line further
    return (lt := sum(1 for x in word if x.isalpha()), len(word) - lt)


def test_count_letters():
    word = 'Hello world!'
    res = count_letters(word)
    exp = (10, 2)
    not_exp = (0, 4)
    assert res == exp, f'input = {word}, expected {exp}, got {res}'
    try:
        assert res == not_exp, word
    except AssertionError:
        pass
    else:
        print(f'input = {word}, expected not {not_exp}')
