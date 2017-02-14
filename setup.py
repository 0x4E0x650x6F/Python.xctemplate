#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
" ___FILENAME___
" ___PROJECTNAME___
"
" Created by ___FULLUSERNAME___ on ___DATE___.
" Copyright ___YEAR___ ___ORGANIZATIONNAME___. All rights reserved.
"""

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='___PROJECTNAME___',
    version='0.1.0',
    description='',
    long_description=readme,
    author='___FULLUSERNAME___',
    author_email='',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
