#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='net_tools',
      version='0.1',
      description='Network Tools',
      author='Robert Mele',
      py_modules=['net_tools'],
      zip_safe=False,
      )
