#!/usr/bin/env python

from distutils.core import setup

setup(name='firehoseui',
    version='0.0.1',
    description='UI for interacting with compiler and static analysis warnings',
    packages=('firehoseui',),
    license='GPL3',
    author='David Malcolm',
    url='https://github.com/fedora-static-analysis/firehoseui',
    classifiers=(
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    )
)
