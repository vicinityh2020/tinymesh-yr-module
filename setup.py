try:
    from setuptools import setup
except ImportError:
    # so that the < v1.5.2 peasants can still run setup.py
    from distutils.core import setup

__version__ = '1.0.0'

NAME = 'tinymesh-yr'
PACKAGES = ['yr']

setup(
    name=NAME,
    packages=PACKAGES,
    install_requires=['requests'],
    version=__version__,
    test_suite='tests',
    description="Python app to retrieve YR weather temperature and precipitation",
    author="German Poljakov",
    author_email="german@tiny-mesh.com",
    url="https://github.com/vicinityh2020/tinymesh-yr-module",
    license='MIT',
    zip_safe=False
)
