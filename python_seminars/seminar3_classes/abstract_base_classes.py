# import collections.abc
from abc import abstractmethod, ABC


class PokemonTrainInterface(ABC):
    @abstractmethod
    def increase_experience(self, value: int):
        pass

    @property
    @abstractmethod
    def experience(self):
        pass


class BasePokemon(PokemonTrainInterface):
    def __init__(self, name, category, initial_experience=100):
        self.name = name
        self.category = category
        self.experience_level = initial_experience

    def __str__(self):
        return f'{self.name}/{self.category}'

    @property
    def experience(self):
        return self.experience_level

    def increase_experience(self, value: int):
        self.experience_level += value


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
    bulbasaur = Pokemon(name='Bulbasaur', category='grass', weaknesses=('first', 'second'))
    bulbasaur.increase_experience(100)
    assert bulbasaur.experience == 200, 'Try harder, Neeman'
