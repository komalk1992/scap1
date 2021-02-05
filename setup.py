# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in scap1/__init__.py
from scap1 import __version__ as version

setup(
	name='scap1',
	version=version,
	description='scap1',
	author='sprics',
	author_email='info@sprics.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
