# setup.py
from setuptools import setup, find_packages

setup(
    name="xbrl_parser",
    version="1.0.0",
    author="ontology",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4>=4.9.0",
        "lxml>=4.6.0",
    ],
)