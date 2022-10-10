class BaseEstimator:
    def to_str(self):
        return f'{self.__class__.__name__}'


# Override method
class CountVectorizer(BaseEstimator):
    def to_str(self):
        base_str = BaseEstimator.to_str(self)
        return f'[{base_str}]'


CountVectorizer().to_str()

