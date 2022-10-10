class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f'{self.name}/{self.category}'


class Pokemon(BasePokemon):
    def __init__(self, name, category, weaknesses):
        self.weaknesses = weaknesses
        super().__init__(name=name, category=category)

    @property
    def weakness(self):
        return self.weaknesses[0]


if __name__ == '__main__':
    base_charmander = BasePokemon(name='Charmander', category='Lizard')
    print(base_charmander)
    bulbasaur = Pokemon(
        name='Bulbasaur',
        category='seed',
        weaknesses=('fire', 'psychic', 'flying', 'ice')
    )
    print(bulbasaur.weakness)
