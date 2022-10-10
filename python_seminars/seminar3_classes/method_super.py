class BaseEstimator:
    def to_str(self):
        return f'{self.__class__.__name__}'


# Override method
class CountVectorizer(BaseEstimator):
    def to_str(self):
        # super() addresses parent class + do not need to call "self"
        base_str = super().to_str()
        return f'[{base_str}]'


CountVectorizer().to_str()
