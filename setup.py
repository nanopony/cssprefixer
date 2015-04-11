#!/usr/bin/env python
#import sys
from setuptools import setup, find_packages

# if sys.version < '2.5':
#     sys.exit('Python 2.5 or higher is required')

setup(name='cssprefixer_py3',
      version='0.0.1',
      description="A tool that rewrites your CSS files, adding vendor-prefixed versions of CSS3 rules. ",
     long_description="""
     Based on cssprefixer by myfreeweb (floatboth@me.com).
     """,
      license='Apache License 2.0',
      author='nanopony',
      author_email='sddeath@gmail.com',
      url='https://github.com/nanopony/cssprefixer',
      requires=['cssutils'],
      include_package_data=True,
      packages=find_packages(),
      keywords=['CSS', 'Cascading Style Sheets', 'Cleanup', 'prefix'],
      classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
      ],
      package_data={},
      entry_points = {
        'console_scripts' : [
          'prefixize = cssprefixer.prefixize:main',
        ]
      },
)
