class Pokemon:
    r"""
    Creates a Pokemon object

    >>> Pokemon(name='Bulbasaur', poketype='grass').__str__()
    'Bulbasaur/grass'
    >>> Pokemon(name='Pikachu', poketype='electric\r\npower').__str__()
    'Pikachu/electric\r\npower'
    >>> Pokemon(name='Squirtle', poketype='water' * 30).__str__()
    'Squirtle/waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater'
    """
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'
