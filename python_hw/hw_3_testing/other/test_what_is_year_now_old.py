import pytest
from unittest.mock import patch, MagicMock
from what_is_year_now import what_is_year_now


@pytest.mark.parametrize("date_format,expected_year",
                         [('2019-03-01', 2019),
                          ('01.03.2019', 2019),
                          ('2022-10-10T19:32Z', 2022),
                          ('1998-08-02', 1998),
                          ('08.02.2000T19:32Z', 2000)])
def test_cases(date_format: str, expected_year: int):
    with patch("what_is_year_now.urllib.request.urlopen") as mocked_get_website:
        mr = MagicMock()
        mr.read.return_value = '{"$id":"1","currentDateTime":"' + date_format + '","utcOffset":"00:00:00",' \
                               '"isDayLightSavingsTime":false,"dayOfTheWeek":"Monday",' \
                               '"timeZoneName":"UTC","currentFileTime":133099034562560989,' \
                               '"ordinalDate":"2022-283","serviceResponse":null}'
        mr.__enter__.return_value = mr
        mocked_get_website.return_value = mr
        assert what_is_year_now() == expected_year, f'input: {date_format}, expected: {expected_year}, got: {mr}'
        mocked_get_website.assert_called_once()
