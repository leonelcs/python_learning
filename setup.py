# -*- coding: utf-8 -*-

# Learn more: https://github.com/leonelcs/python_learning/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python_learning',
    version='0.1.0',
    description='Learning Projects',
    long_description=readme,
    author='Leonel Cândido da Silva',
    author_email='leonelcs@gmail.com',
    url='https://github.com/leonelcs/python_learning',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)