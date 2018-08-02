try:
    from setuptools import setup
except ImportError:
    # so that the < v1.5.2 peasants can still run setup.py
    from distutils.core import setup

__version__ = '1.0.0'

NAME = 'yr'
PACKAGES = ['yr']

setup(
    name=NAME,
    packages=PACKAGES,
    install_requires=['requests'],
    version=__version__,
    test_suite='tests',
    description="Python app to retrieve yr weather temperature and precipitation",
    author="German Poljakov",
    author_email="hi@example.com",
    url="",
)
