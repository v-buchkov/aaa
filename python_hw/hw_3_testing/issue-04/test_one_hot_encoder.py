import pytest
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


@pytest.fixture
def english_football_teams():
    return ['Manchester United', 'Everton', 'Nottingham Forest', 'Manchester United', 'Leeds United']


@pytest.fixture
def heavy_metal_bands():
    return ['Metallica', 'Black Sabbath', 'Iron Maiden', 'Iron Maiden', 'Metallica']


# Check for standard output (using fixture)
def test_standard(english_football_teams):
    input_data = english_football_teams
    res = fit_transform(input_data)
    exp = [('Manchester United', [0, 0, 0, 1]),
           ('Everton', [0, 0, 1, 0]),
           ('Nottingham Forest', [0, 1, 0, 0]),
           ('Manchester United', [0, 0, 0, 1]),
           ('Leeds United', [1, 0, 0, 0])]
    assert res == exp, f'input: {input_data}, expected: {exp}, got: {res}'


# Check that TypeError is raised, when no argument is passed
def test_no_argument():
    with pytest.raises(TypeError):
        fit_transform()


# Check that each vector consists only of 1 and 0s (using faker)
def test_vector_binary(faker):
    input_data = [faker.name() for i in range(10)]
    print(input_data)
    assert all(i <= 1 for i in
               sum([item[1] for item in fit_transform(input_data)], [])), f'input: {input_data}, ' \
                                                                          f'some vector value is larger than 1'


# Check that in each vector 1 is met only once (using fixture)
def test_one_is_met_only_once(heavy_metal_bands):
    input_data = heavy_metal_bands
    res = [item[1] for item in fit_transform(input_data)]
    for r in res:
        assert sorted(r) == [0] * (len(set(input_data)) - 1) + [1], f'input: {input_data}, met several 1s in vector'


# Check that no exception is raised for list of integers (already pre-defined categories for ML algo)
def test_no_exception():
    input_data = [1, 2, 3, 6]
    assert type(fit_transform(input_data)) == list, f'input: {input_data}, incorrect type returned (not list)'


# Check that list of lists raises TypeError (unhashable)
def test_exception_with_list():
    with pytest.raises(TypeError):
        fit_transform(([4, 7, 8], 6, 7, 0, 2))


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
