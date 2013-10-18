#!/usr/bin/env python

import sys
from os.path import join, dirname
sys.path.append(join(dirname(__file__), 'src'))

from setuptools import setup

from ez_setup import use_setuptools
use_setuptools()

PACKAGE = 'HaiSafari'
VERSION = '1.1.0'
AUTHOR = 'QA automation'
EMAIL = 'qa_automation@hotmail.com'
DESCRIPTION = 'Test Safari webdriver'

VERSION_FILE = '__version__.py'
SOURCE_DIR   = 'src'

execfile(join(dirname(__file__), SOURCE_DIR, 'HaiSafari', VERSION_FILE))


setup(
    name         = 'HaiWebdriver',
    version      = VERSION,
    description  = DESCRIPTION,
    author       = AUTHOR,
    author_email = EMAIL,
    url          = 'https://github.com/may3450/playground/tree/master/HaiWebdriver',
    license      = 'free',
    py_modules   = ['ez_setup'],
    package_dir  = { '' : 'src'},
    packages     = ['HaiSafari'],
    include_package_data = True,
    )
          
