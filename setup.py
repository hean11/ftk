# Setup for ftk

"""setup.py setup for ftk"""

from setuptools import setup

setup(
    name = 'ftk',
    version = '1.0.0',
    url = 'http://www.sitec-systems.de',
    license = 'LGPLv2',
    author = 'Robert Lehmann',
    author_email = 'robert.lehmann@sitec-systems.de',
    packages = ['ftk', 'ftk.recovery'],
    scripts = ['scripts/ftk'],
)
