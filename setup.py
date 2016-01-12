#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path

description = file(
    os.path.join(os.path.dirname(__file__), 'README.rst'), 'rb').read()

setup(
    name="treeshape",
    version="0.1.0",
    description="Quickly make files and directory structures.",
    long_description=description,
    author="Jonathan Lange",
    author_email="jml@mumak.net",
    install_requires=[
        "fixtures",
        "testtools",
        ],
    zip_safe=False,
    packages=find_packages('.'),
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        ],
)
