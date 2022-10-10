class BaseEstimator:
    def to_str(self):
        return f'{self.__class__.__name__}'


class CountVectorizer(BaseEstimator):
    def __init__(self):
        self._stop_words = ('and', 'or', 'the')


CountVectorizer().to_str()
