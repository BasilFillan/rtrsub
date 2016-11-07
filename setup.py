#!/usr/bin/env python
# Copyright (C) 2016 Job Snijders <job@instituut.net>
#
# This file is part of rtrsub
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF  THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import rtrsub
version = rtrsub.__version__

import codecs
import os
import sys

from setuptools import setup, find_packages
from os.path import abspath, dirname, join

here = abspath(dirname(__file__))

with codecs.open(join(here, 'README.md'), encoding='utf-8') as f:
    README = f.read()

if sys.argv[-1] == 'publish':
    os.system('python2.7 setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print(("  git tag -a %s -m 'version %s'" % (version, version)))
    print("  git push --tags")
    sys.exit()

install_reqs = parse_requirements('requirements.txt', session="")
reqs = [str(ir.req) for ir in install_reqs]


setup(
    name='rtrsub',
    version=version,
    maintainer="Job Snijders",
    maintainer_email='job@instituut.net',
    url='https://github.com/job/rtrsub',
    description='RTR Substitution',
    long_description=README,
    license='BSD 2-Clause',
    keywords='rpki prefix routing networking',
    setup_requires=reqs,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3 :: Only'
    ],
    packages=find_packages(exclude=['tests', 'tests.*']),
    entry_points={'console_scripts': ['rtrsub = rtrsub.cli:main']},
)
