#!/usr/bin/env python

from distutils.core import setup

setup(name='myUniqueAnalytics',
      version='1.2dev',
      packages=['analytics', 'analytics.test'],
      scripts=['bin/excel2Json.py','bin/json2Excel.py'],
      description='Python setup test',
      license='LICENSE.txt',
      author='YDD9',
      author_email='YDD9@unknown.org',
      url='https://github.com/YDD9/testTodelete.git/',
      long_description=open('README.mk').read(),
	  install_requires=[
        "Django >= 1.1.1",
        "caldav == 0.1.4",
      ],
     )