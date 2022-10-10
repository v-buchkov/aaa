class BaseEstimator:
    def to_str(self):
        return f'{self.__class__.__name__}'


class BaseVectorizer:
    def get_stop_words(self):
        return self._stop_words


class CountVectorizer(BaseEstimator, BaseVectorizer):
    def __init__(self):
        self._stop_words = ('and', 'or', 'the')


print(CountVectorizer().to_str())
print(CountVectorizer.mro())
