class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f'{self.name}/{self.category}'


class EmojiMixin(BasePokemon):
    EMOJI_DICT = {'grass': '🌿', 'fire': '🔥', 'water': '🌊', 'electric': '⚡'}

    def __str__(self):
        name, category = super().__str__().split('/')
        return f'{name}/{self.EMOJI_DICT[category]}'


class Pokemon(EmojiMixin, BasePokemon):
    def __init__(self, name, category, weaknesses):
        self.weaknesses = weaknesses
        super().__init__(name=name, category=category)

    @property
    def weakness(self):
        return self.weaknesses[0]


if __name__ == '__main__':
    bulbasaur = Pokemon(
        name='Bulbasaur',
        category='grass',
        weaknesses=('fire', 'psychic', 'flying', 'ice')
    )
    print(bulbasaur)
