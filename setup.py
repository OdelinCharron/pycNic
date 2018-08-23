# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='core',
    version='0.0.1',
    description='Automated quiz for mri images',
    long_description=readme,
    author='Odelin Charron, Vincent Noblet',
    author_email='audy322@hotmail.fr',
    url='https://github.com/OdelinCharron/core',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'examples'))
)