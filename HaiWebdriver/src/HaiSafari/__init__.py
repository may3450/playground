#!/usr/bin/python
# -*- coding: utf8 -*-

from .firefox.webdriver import WebDriver as Firefox
from .firefox.firefox_profile import FirefoxProfile
from .chrome.webdriver import WebDriver as Chrome
from .chrome.options import Options as ChromeOptions
from .ie.webdriver import WebDriver as Ie
from .opera.webdriver import WebDriver as Opera
from .phantomjs.webdriver import WebDriver as PhantomJS
from .remote.webdriver import WebDriver as Remote
from .common.desired_capabilities import DesiredCapabilities
from .common.action_chains import ActionChains
from .common.touch_actions import TouchActions
from .common.proxy import Proxy
from .safari.webdriver import WebDriver as Safari

__version__ = '2.35.0'

