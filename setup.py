#!/usr/bin/env python3
'''
Setup for pyfos
'''
from setuptools import setup, find_packages

setup(
	name='pyfos',
	version='0.9.0',
	description='Brocade FOS Library.',
	author='Brocade Communications Systems, Inc.',
	author_email='automation@brocade.com',
	url='http://www.brocade.com/',
	packages=find_packages(),
	install_requires=[
		'xmltodict',
		'requests',
		'jsondiff'
	],
)
