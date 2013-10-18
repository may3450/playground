#!/usr/bin/python
# -*- coding: utf8 -*-

import base64

try:
    import http.client as http_client
except ImportError:
    import httplib as http_client

import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from .service import Service

class WebDriver(RemoteWebDriver):
    """
    Controls the SafariDriver and allows you to drive the browser.
    
    """

    def __init__(self, executable_path='Safari.exe', port=0,
                 desired_capabilities=DesiredCapabilities.SAFARI):
        """
        Creates a new instance of the Safari driver.

        Starts the service and then creates new instance of Safari Driver.

        :Args:
         - executable_path - path to the executable. If the default is used it assumes the executable is in the
           Environment Variable SELENIUM_SERVER_JAR
         - port - port you would like the service to run, if left as 0, a free port will be found.
         - desired_capabilities: Dictionary object with desired capabilities (Can be used to provide various Safari switches).
        """
        if executable_path is None:
            try:
                executable_path = os.environ["SELENIUM_SERVER_JAR"]
            except:
                raise Exception("No executable path given, please add one to Environment Variable \
                'SELENIUM_SERVER_JAR'")
        self.service = Service(executable_path, port=port)
        self.service.start()

        RemoteWebDriver.__init__(self,
            command_executor=self.service.service_url,
            desired_capabilities=desired_capabilities)
        self._is_remote = False

    def quit(self):
        """
        Closes the browser and shuts down the SafariDriver executable
        that is started when starting the SafariDriver
        """
        try:
            RemoteWebDriver.quit(self)
        except http_client.BadStatusLine:
            pass
        finally:
            self.service.stop()
