import os
import unittest
from unittest import mock
from yr import Weather


def mocked_requests_get(**kwargs):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mocks', 'mock_forecast.xml')
    with open(file_path, 'r') as f:
        mock_xml = f.read()

    class MockResponse:
        def __init__(self, xml_data, status_code):
            self.text = xml_data
            self.status_code = status_code

    return MockResponse(mock_xml, 200)


class TestWeather(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):

        expected_temperature = 25
        expected_precipitation = 0.0

        yr = Weather()

        t, p = yr.get_forecast('Oslo')

        self.assertEqual(expected_temperature, t, 'Expected: %d. Got: %d' % (expected_temperature, t))
        self.assertEqual(expected_precipitation, p, 'Expected: %.1f. Got: %.1f' % (expected_precipitation, p))


if __name__ == '__main__':
    unittest.main()