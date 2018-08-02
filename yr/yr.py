import requests

from requests.status_codes import codes
from requests.exceptions import ConnectionError

import xml.etree.ElementTree as Xml

from datetime import datetime, timezone, timedelta


class Weather:
    def __init__(self):
        self.__scheme = 'https://'
        self.__host = 'www.yr.no'

        # simple in-memory cache stores a entries of list of
        # [0]: last_modified
        # [1]: temperature
        # [2]: precipitation
        self.__cache = {}

        # cache threshold
        self.__cache_threshold = timedelta(minutes=10)

    def __str__(self):
        return '%s%s' % (self.__scheme, self.__host)

    def __repr__(self):
        return '%s%s' % (self.__scheme, self.__host)

    def get_forecast(self, town: str, country: str = 'Norway') -> (int, float):
        cache_key = '{}+{}'.format(country, town)

        cached_result = self.__get_cache(cache_key)
        if cached_result:
            return cached_result[0], cached_result[1]

        url = '{scheme}{host}/place/{c}/{t}/{t}/{t}/forecast.xml'.format(
            scheme=self.__scheme, host=self.__host, c=country, t=town)

        try:
            res = requests.get(url=url)
        except ConnectionError as e:
            print(e.strerror)
            return None, None

        if res.status_code != codes.OK:
            print("could not get the weather data for ({}, {}).\n".format(town, country))
            return None, None

        if not hasattr(res, 'text'):
            print("response has no text attribute.\n")
            return None, None

        yr_xml = Xml.fromstring(res.text)
        forecast = yr_xml.find('forecast').find('tabular').find('time')

        temperature = forecast.find('temperature').attrib['value']
        precipitation = forecast.find('precipitation').attrib['value']

        temperature = int(temperature)
        precipitation = float(precipitation)

        self.__set_cache(cache_key, temperature, precipitation)
        return temperature, precipitation

    def __get_cache(self, key) -> list:
        if key in self.__cache:
            cached_entry = self.__cache[key]

            # checks if the cached entry was stored X-minutes or less ago, then return
            # otherwise return an empty list
            last_modified = cached_entry[0]
            if datetime.now(tz=timezone.utc) - last_modified <= self.__cache_threshold:
                return [cached_entry[1], cached_entry[2]]
        return []

    def __set_cache(self, key, t, p):
        self.__cache[key] = [datetime.now(tz=timezone.utc), t, p]
