import pytest
from unittest.mock import patch, MagicMock
from what_is_year_now import what_is_year_now


def get_json_str(date_format: str):
    return '{"$id":"1","currentDateTime":"' + date_format + '","utcOffset":"00:00:00",' \
                                                            '"isDayLightSavingsTime":false,' \
                                                            '"dayOfTheWeek":"Monday","timeZoneName":"UTC",' \
                                                            '"currentFileTime":133099034562560989,' \
                                                            '"ordinalDate":"2022-283","serviceResponse":null}'


def get_wrong_json_str(date_format: str):
    return '{"$id":"1","DateTime":"' + date_format + '","utcOffset":"00:00:00",' \
                                                     '"isDayLightSavingsTime":false,' \
                                                     '"dayOfTheWeek":"Monday","timeZoneName":"UTC",' \
                                                     '"currentFileTime":133099034562560989,' \
                                                     '"ordinalDate":"2022-283","serviceResponse":null}'


def patch_caller(return_value) -> int:
    with patch("what_is_year_now.urllib.request.urlopen") as mocked_get_website:
        mr = MagicMock()
        mr.read.return_value = return_value
        mr.__enter__.return_value = mr
        mocked_get_website.return_value = mr
        return what_is_year_now()


@pytest.mark.parametrize("date,expected_year",
                         [('2019-03-01', 2019),
                          ('01.03.2019T19:32Z', 2019),
                          ('2022-10-10T19:32Z', 2022),
                          ('1998-08-02', 1998),
                          ('08.02.2000', 2000)])
def test_cases(date: str, expected_year: int):
    mocked_json = get_json_str(date)
    res = patch_caller(mocked_json)
    assert res == expected_year, f'input: {date}, expected: {expected_year}, got: {res}'


def test_value_error():
    mocked_json = get_json_str('deeifjifnmfifr')
    with pytest.raises(ValueError):
        patch_caller(mocked_json)


def test_not_json_input():
    with pytest.raises(TypeError):
        patch_caller(lambda x: x)


def test_key_error():
    mocked_json = get_wrong_json_str('08.02.2000')
    with pytest.raises(KeyError):
        patch_caller(mocked_json)


def test_type_output():
    date = '08.02.2000'
    mocked_json = get_json_str(date)
    res = patch_caller(mocked_json)
    assert type(res) == int, f'input: {date}, expected: int, got: {type(res)}'


def test_index_error_ymd():
    date = '0'
    with pytest.raises(IndexError):
        mocked_json = get_json_str(date)
        patch_caller(mocked_json)


def test_index_error_dmy():
    date = '08702'
    with pytest.raises(IndexError):
        mocked_json = get_json_str(date)
        patch_caller(mocked_json)


def test_value_error_output():
    date = '08.02.VVVV'
    with pytest.raises(ValueError):
        mocked_json = get_json_str(date)
        patch_caller(mocked_json)
