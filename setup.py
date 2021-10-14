#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup
from pathlib import Path


def get_version(filepath):
    var = {}
    for line in Path(filepath).read_text().splitlines():
        if '__version__' in line:
            exec(line, var)
    return var['__version__']


version = get_version('tradernet/__init__.py')
description = Path('docs/README.rst').read_text()

install_requirements = [
    'urllib3',
    'requests',
]

setup_requirements = [
    # put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # put package test requirements here
]

setup(
    name='tradernet',
    version=version,
    description="Interact with Tradernet API",
    long_description=description,
    author="Dmytro Kazanzhy",
    author_email='dkazanzhy@gmail.com',
    url='https://github.com/kazanzhy/tradernet',
    download_url='https://github.com/kazanzhy/tradernet/tarball/main',
    packages=["tradernet"],
    package_dir={"tradernet": "./tradernet"},
    test_suite='tests',
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=install_requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    license="MIT license",
    zip_safe=False,
    keywords='tradernet',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
