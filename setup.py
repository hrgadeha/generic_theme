# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
try: # for pip >= 10
   from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
  from pip.req import parse_requirements
import re, ast

version = '0.0.1'
requirements = parse_requirements("requirements.txt", session="")

setup(
	name='generic_theme',
	version=version,
	description='Generic ERPNext Website Theme',
	author='Said Salameh',
	author_email='ss@saidsalameh.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir.req) for ir in requirements],
	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
