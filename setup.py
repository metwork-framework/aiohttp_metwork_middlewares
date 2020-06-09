#!/usr/bin/env python
import fastentrypoints  # noqa: F401
import sys
from setuptools import setup
from setuptools import find_packages

required = []
dependency_links = []
EGG_MARK = '#egg='
with open('requirements.txt') as reqs:
    for line in reqs.read().split('\n'):
        if line.startswith('-e git:') or line.startswith('-e git+') or \
                line.startswith('git:') or line.startswith('git+'):
            if EGG_MARK in line:
                package_name = line[line.find(EGG_MARK) + len(EGG_MARK):]
                required.append(package_name)
                dependency_links.append(line)
            else:
                print('Dependency to a git repository should have the format:')
                print('git+ssh://git@github.com/xxxxx/xxxxxx#egg=package_name')
                sys.exit(1)
        else:
            required.append(line)

DESCRIPTION = ("Automatic mflog/nginx correlation for request_id (Metwork usage)")

setup(
    name="aiohttp_metwork_middlewares",
    version="0.0.1",
    packages=find_packages()
    install_requires=required,
    dependency_links=dependency_links,
    zip_safe=False
)
