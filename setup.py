#!/usr/bin/env python

import os
import platform
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "1.0"

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name='cookiecutter-django',
    version=version,
    description='A Cookiecutter template for creating production-ready Django projects quickly.',
    long_description=long_description,
    author='Daniel Roy Greenfeld',
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/cookiecutter-django',
    packages=[],
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    keywords=(
        'cookiecutter, Python, projects, project templates, django, '
        'skeleton, scaffolding, project directory, setup.py'
    ),
)