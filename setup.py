#!/usr/bin/env python3
'''
Setup for pyfos
'''
from setuptools import setup, find_packages
import re

exec(open('pyfos/version.py').read())
req_file = 'requirements.txt'

def get_required_packages():
    packages = []
    with open(req_file) as req:
        for line in req:
            line = line.strip()
            # Skip comment lines
            if re.search(r'\s*#', line) is not None:
                continue
            if not line:
                continue
            packages.append(line)
    req.close()

    return packages

with open("README.md", "r") as fh:
        long_description = fh.read()
fh.close()

setup(
	name='pyfos',
	version=__version__,
	description='Brocade FOS Library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
	author='Brocade Communications Systems LLC.',
	author_email='Automation.BSN@broadcom.com',
	url='http://www.brocade.com/',
	packages=find_packages(),
    install_requires=get_required_packages(),
    zip_safe=False,
)
