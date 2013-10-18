#!/usr/bin/python
# -*- coding: utf8 -*-

import subprocess
from subprocess import PIPE
import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common import utils

class Service(object):
    """
    Object that manages the starting and stopping of the safariDriver 
    """

    def __init__(self, executable_path, port=0):
        """
        Creates a new instance of the Service
        
        :Args:
         - executable_path : Path to the safariDriver
         - port : Port the service is running on """

        self.port = port
        self.path = executable_path
        if self.port == 0:
            self.port = utils.free_port()

    def start(self):
        """
        Starts the safariDriver Service. 
        
        :Exceptions:
         - WebDriverException : Raised either when it can't start the service
           or when it can't connect to the service
        """
        try:
            self.process = subprocess.Popen(["java", "-jar", self.path, "-port", "%s" % self.port])
        except:
            raise WebDriverException(
                "safariDriver executable needs to be available in the path. \
                ")
        time.sleep(10)
        count = 0
        while not utils.is_connectable(self.port):
            count += 1
            time.sleep(1)
            if count == 30:
                 raise WebDriverException("Can not connect to the safariDriver")
                
    @property
    def service_url(self):
        """
        Gets the url of the safariDriver Service
        """
        return "http://localhost:%d/wd/hub" % self.port

    def stop(self):
        """ 
        Tells the safariDriver to stop and cleans up the process
        """
        #If its dead dont worry
        if self.process is None:
            return

        self.process.kill()
        self.process.wait()

