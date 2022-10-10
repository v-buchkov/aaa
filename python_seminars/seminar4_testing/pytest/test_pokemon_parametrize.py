class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


def test_standard(self):
    res = Pokemon(name='Bulbasaur', poketype='grass').__str__()
    exp = 'Bulbasaur/grass'
    self.assertEqual(res, exp)


def test_special_symbols(self):
    res = Pokemon(name='Pikachu', poketype='electric\r\npower').__str__()
    exp = 'Pikachu/electric\r\npower'
    self.assertEqual(res, exp)


def test_with_formula(self):
    res = Pokemon(name='Squirtle', poketype='water' * 30).__str__()
    exp = 'Squirtle/waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater' \
          'waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater'
    self.assertEqual(res, exp)
