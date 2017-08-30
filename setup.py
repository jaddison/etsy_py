#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import etsy_py

setup(
    name='etsy_py',
    version=etsy_py.__version__,
    description="Python2 & Python3 module for Etsy's API.",
    long_description=open('README.md').read(),
    author='James Addison',
    author_email='addi00+github.com@gmail.com',
    url=etsy_py.repo_url,
    license="BSD",
    packages=[
        'etsy_py'
    ],
    install_requires=[
        'requests',
        'six'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
