# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in test_app/__init__.py
from test_app import __version__ as version

setup(
	name='test_app',
	version=version,
	description='test',
	author='frappe',
	author_email='saroj@bloomstack.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
