class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


def test_standard():
    res = Pokemon(name='Bulbasaur', poketype='grass').__str__()
    exp = 'Bulbasaur/grass'
    assert res == exp


def test_special_symbols():
    res = Pokemon(name='Pikachu', poketype='electric\r\npower').__str__()
    exp = 'Pikachu/electric\r\npower'
    assert res == exp


def test_with_formula():
    res = Pokemon(name='Squirtle', poketype='water' * 30).__str__()
    exp = 'Squirtle/waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater' \
          'waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater'
    assert res == exp
