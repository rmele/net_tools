#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='net_tools',
      version='0.1',
      description='Network Tools',
      author='Robert Mele',
      author_email='rmorlando@gmail.com',
      py_modules=['net_tools'],
      url='https://www.wintermute.com',
      zip_safe=False,
      )
