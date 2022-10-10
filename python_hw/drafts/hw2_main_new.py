"""
Buchkov Viacheslav, DS Track, Python - HW2
"""
import json


class DictToAttrs:
    """
    This class reads the dictionary and creates the attributes from key-value pairs
    ! Class is not specific to this HW and can be fully reused in further applications

    ! If some value is also dict-type, the class will create attributes OF ANY DEPTH
    (E.g., if some key returns dict with some value as also a dict, the class creates attributes for all inner dicts)
    """
    def __init__(self, input_dict: dict):
        # Set initial attributes (decompose first-level dict)
        self.set_attributes(self, input_dict, '_')
        # Decompose all inner dicts
        self.decompose_all_dicts()

    # Method for setting attributes to an object from a dict
    @staticmethod
    def set_attributes(obj: object, python_dict: dict, privatness: str = '') -> None:
        for key, value in python_dict.items():
            setattr(obj, privatness + key, value)

    # Method that operates with inner dicts, decomposing all into sub-attrs to the main attr - key to this dict
    def decompose_inner_attributes(self) -> None:
        # List of attribute names
        attr_names = list(vars(self))
        for attr_name in attr_names:
            # Value for the given attribute
            attr_obj = getattr(self, attr_name)
            # If the attr name corresponds to a dict, should decompose
            if type(attr_obj) == dict:
                # Set attr as function to add sub-attrs
                setattr(self, attr_name, lambda: getattr(self, attr_name))
                # Set sub-attrs to attr
                self.set_attributes(getattr(self, attr_name), attr_obj)
        # List of types of attribute values
        attr_types = [type(getattr(self, name)) for name in attr_names]
        return attr_types

    # Method to decompose all inner dicts iteratively
    def decompose_all_dicts(self) -> None:
        # Decompose first dicts (if any) and get all the types
        attr_types = self.decompose_inner_attributes()
        # Repeat iteratively, while at least one not decomposed dict left
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
        self.rename_super_attrs()
        self.check_required_inputs()

    def rename_super_attrs(self):
        for key, value in dict(vars(self)).items():
            new_key = key.lstrip('_')
            if new_key not in dir(self):
                setattr(self, new_key, value)

    def check_required_inputs(self):
        requirements = ['_' + req_input in list(vars(self)) for req_input in self.REQUIRED_INPUTS]
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
    print(advert.location.address)
    print(advert.price)

    print(advert)
