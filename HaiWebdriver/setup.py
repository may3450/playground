#!/usr/bin/env python

import sys
from os.path import join, dirname
sys.path.append(join(dirname(__file__), 'src'))

from setuptools import setup
from shutil import rmtree

from ez_setup import use_setuptools
use_setuptools()

PACKAGE = 'HaiSafari'
VERSION = '1.1.0'
AUTHOR = 'QA automation'
EMAIL = 'qa_automation@hotmail.com'
DESCRIPTION = 'Test Safari webdriver'
INSTALL_REQUIRES = [ "HaiSafari == 1.1.0"]

VERSION_FILE = '__version__.py'
SOURCE_DIR   = 'src'

execfile(join(dirname(__file__), SOURCE_DIR, 'HaiSafari', VERSION_FILE))


setup(
    name         = PACKAGE,
    version      = VERSION,
    description  = DESCRIPTION,
    author       = AUTHOR,
    author_email = EMAIL,
    url          = 'https://github.com/may3450/playground/tree/master/HaiWebdriver',
    license      = 'free',
    py_modules   = ['ez_setup'],
    package_dir  = { '' : 'src'},
    packages     = ['HaiSafari'],
    package_data     = {PACKAGE: ['*/*.py', '*/*/*.py', '*/*/*/*.py']},
    install_requires = INSTALL_REQUIRES
    )
          
rmtree('./src/%s.egg-info' % PACKAGE, True)
