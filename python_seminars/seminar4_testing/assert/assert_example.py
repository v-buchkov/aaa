class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


def test_pokemon(name: str, poketype: str, exp: str, not_exp: str):
    res = Pokemon(name=name, poketype=poketype)
    assert res.__str__() == exp, f'input = {name, poketype}, expected {exp}, got {res}'
    try:
        assert res.__str__() == not_exp
    except AssertionError:
        pass
    else:
        print(f'input = {name, poketype}, expected not {not_exp}')


test_pokemon(name='Bulbasaur', poketype='grass', exp='Bulbasaur/grass', not_exp='Bulbasaur / grass')
test_pokemon(name='Pikachu', poketype='electric\r\npower', exp='Pikachu/electric\r\npower',
             not_exp='Pikachu/electric\tpower')
test_pokemon(name='Squirtle', poketype='water' * 30,
             exp='Squirtle/waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater'
                 'waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater', not_exp="Squirtle/'water' * 30")
