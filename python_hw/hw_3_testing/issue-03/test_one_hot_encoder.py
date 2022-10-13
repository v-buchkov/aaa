import unittest
from typing import List, Tuple


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestOneHotEncoder(unittest.TestCase):

    # Check for standard output
    def test_standard(self):
        res = fit_transform(['Manchester United',
                             'Everton',
                             'Nottingham Forest',
                             'Manchester United',
                             'Leeds United'])
        exp = [('Manchester United', [0, 0, 0, 1]),
               ('Everton', [0, 0, 1, 0]),
               ('Nottingham Forest', [0, 1, 0, 0]),
               ('Manchester United', [0, 0, 0, 1]),
               ('Leeds United', [1, 0, 0, 0])]
        self.assertListEqual(res, exp)

    # Check that TypeError is raised, when no argument is passed
    def test_no_argument(self):
        self.assertRaises(TypeError, lambda: fit_transform())

    # Check that each vector consists only of 1 and 0s
    def test_vector_binary(self):
        self.assertNotIn(2, [item[1] for item in fit_transform(['Metallica',
                                                                'Black Sabbath',
                                                                'Iron Maiden',
                                                                'Iron Maiden',
                                                                'Metallica'])])

    # Check that in each vector 1 is met only once
    def test_one_is_met_only_once(self):
        input_data = ['Metallica',
                      'Black Sabbath',
                      'Iron Maiden',
                      'Iron Maiden',
                      'Metallica']
        res = [item[1] for item in fit_transform(input_data)]
        for r in res:
            self.assertTrue(sorted(r) == [0] * (len(set(input_data)) - 1) + [1])

    # Check that no exception is raised for list of integers (already pre-defined categories for ML algo)
    def test_no_exception(self):
        self.assertIsInstance(fit_transform([1, 2, 3, 6]), list)

    # Check that list of lists raises TypeError (unhashable)
    def test_exception_with_list(self):
        self.assertRaises(TypeError, lambda: fit_transform(([4, 7, 8], 6, 7, 0, 2)))


if __name__ == '__main__':
    from pprint import pprint

    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    pprint(transformed_cities)
    assert transformed_cities == exp_transformed_cities
