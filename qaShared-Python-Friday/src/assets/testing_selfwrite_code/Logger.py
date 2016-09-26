# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 18:47:05 2016

@author: user
"""

import logging

class Logger(object):
    """ Logger: The Logger object creates a new log file or appends to one
        which was created previously. It accepts one parameter, guiOrTui, which
        holds a string of the class the logger is being called from, so if the
        logger is called from mainGUI, it will be "GUI". This is to differentiate
        between log messages from the TUI or GUI. """
    def __init__(self, guiOrTui):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        self.fh = logging.FileHandler('assets/ASAS_Log.log')
        self.fh.setLevel(logging.DEBUG)
        self.fh.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.info('---------- Started logging %s ----------' % (guiOrTui))
    
    def getLogger(self):
        """ getLogger: This method returns the logger object which can be used
            to log INFO/DEBUG messages. """
        return self.logger
        
    def getFileHandler(self):
        """ getFileHandler: This method returns the file handler for the
            logger, which allows the logger file to be closed when the program
            quits. """
        return self.fh