"""
Buchkov Viacheslav, DS Track, Python - HW2
"""
import json


class DictToAttrs:
    """
    This class reads the dictionary and creates the attributes from key-value pairs

    ! If some value is also dict-type, the class will create attributes OF ANY DEPTH
    (E.g., if some key returns dict with some value as also a dict, the class creates attributes for all inner dicts)
    """
    def __init__(self, input_dict: dict):
        # Set initial attributes (decompose first-level dict)
        self.set_attributes(self, input_dict)
        # Decompose all inner dicts
        self.decompose_all_dicts()

    # Method for setting attributes to an object from a dict
    @staticmethod
    def set_attributes(obj: object, python_dict: dict):
        for key, value in python_dict.items():
            if key == 'price':
                key = '_price'
            setattr(obj, key, value)

    def decompose_inner_attributes(self):
        attr_names = list(vars(self))
        attr_types = [type(getattr(self, name)) for name in attr_names]
        for attr_name in attr_names:
            attr_obj = getattr(self, attr_name)
            if type(attr_obj) == dict:
                setattr(self, attr_name, lambda: getattr(self, attr_name))
                self.set_attributes(getattr(self, attr_name), attr_obj)
        return attr_types

    def decompose_all_dicts(self):
        attr_types = self.decompose_inner_attributes()
        while dict in attr_types:
            attr_types = self.decompose_inner_attributes()


class ColorizeMixin:
    repr_color_code = 33

    def __repr__(self):
        self.repr_starter = f'\033[1;{self.repr_color_code};40m '


class Advert(ColorizeMixin, DictToAttrs):
    REQUIRED_INPUTS = ['title']

    def __init__(self, json_dict):
        super().__init__(json_dict)
        self.check_required_inputs()

    def check_required_inputs(self):
        requirements = [req_input in list(vars(self)) for req_input in self.REQUIRED_INPUTS]
        assert all(requirements), f'Please, check required inputs: {", ".join(self.REQUIRED_INPUTS)}'

    @property
    def price(self, default_value: float = 0):
        advert_price = vars(self).get('_price', default_value)
        if advert_price < 0:
            raise ValueError('Price must be non-negative!')
        return advert_price

    def __repr__(self):
        self.repr_starter = ''
        super().__repr__()
        return self.repr_starter + f'{self.title} | {self.price} RUB'


if __name__ == '__main__':
    json_txt = """{
    "title": "python", "price": 20,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
}"""
    advert_dict = json.loads(json_txt)
    advert = Advert(advert_dict)
    print(advert.location)
    print(advert.location.address)
    print(advert.price)

    print(advert)
