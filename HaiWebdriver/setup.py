#!/usr/bin/env python

from os.path import join, dirname
from setuptools import setup
from shutil import rmtree
import sys
import re
import glob

PACKAGE=None
build = False

if build:
    assert PACKAGE, 'Please provide the package name (should start with Hai) to build distribution for!'

VERSION_FILE = '__version__.py'
SOURCE_DIR   = 'src'

# important for installation procedure (pip install PACKAGE)
# we will get the PACKAGE name from the __file__ value
# __file__ format: .../build/HaiAmazon/setup.py
if not build and not PACKAGE: 
    path_list = dirname(__file__).split('/')
    PACKAGE = path_list[len(path_list)-1]
    # and this part is specific for local installation from dist directory
    # builds is untared in /tmp directory
    glob_list = glob.glob(r'%s/%s/Hai*' % (dirname(__file__), SOURCE_DIR))
    for local in glob_list:
        if re.match(r'.*/Hai[^\./]*$', local): 
            path_list = local.split('/')
            PACKAGE = path_list[len(path_list)-1]

execfile(join(dirname(__file__), SOURCE_DIR, PACKAGE, VERSION_FILE))


setup(
    name         = PACKAGE,
    version      = VERSION,
    description  = DESCRIPTION,
    author       = AUTHOR,
    author_email = EMAIL,
    url          = 'https://stash.haivision.com/projects/QUACK/repos/quack/browse/playground/selenium/HaiWebdriver',
    license      = 'free',
    package_dir  = { '' : 'src'},
    packages     = [PACKAGE],
    package_data     = {PACKAGE: ['*/*.py', '*/*/*.py', '*/*/*/*.py']},
    install_requires = INSTALL_REQUIRES
    )
          
rmtree('./src/%s.egg-info' % PACKAGE, True)
