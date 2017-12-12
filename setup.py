# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='histone_code_vae',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Rick Farouni',
    author_email='rfarouni@gmail.com',
    url='https://github.com/rfarouni/histone_code_vae',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'r_code'))
)

