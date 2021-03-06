#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup


setup(
    name='django-calaccess-raw-data',
    version='0.1.2',
    packages=(
        'calaccess_raw',
        'calaccess_raw.admin',
        'calaccess_raw.management',
        'calaccess_raw.management.commands',
        'calaccess_raw.models',
    ),
    include_package_data=True,
    license='MIT',
    description='A Django app to download, extract and load campaign \
finance and lobbying activity data from the California \
Secretary of State\'s CAL-ACCESS database',
    url='http://django-calaccess-raw-data.californiacivicdata.org/',
    author='California Civic Data Coalition',
    author_email='ben.welsh@latimes.com',
    install_requires=(
        'django>=1.7',
        'csvkit',
        'python-dateutil',
        'requests',
        'clint',
        'hurry.filesize'
    ),
)
