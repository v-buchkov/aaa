import pytest


class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


@pytest.mark.parametrize("name,poketype,exp",
                         [('Bulbasaur', 'grass', 'Bulbasaur/grass'),
                          ('Pikachu', 'electric\r\npower', 'Pikachu/electric\r\npower'),
                          ('Squirtle', 'water' * 30, 'Squirtle/waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater'
                                                     'waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater'
                                                     'waterwaterwaterwaterwaterwater')])
def test_pokemon(name, poketype, exp):
    res = Pokemon(name=name, poketype=poketype).__str__()
    assert res == exp, f'input: {name, poketype}, expected: {exp}, got: {res}'
