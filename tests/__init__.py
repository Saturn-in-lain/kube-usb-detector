"""
Unit tests for parsedatetime
The tests can be run as a C{suite} by running::
    nosetests
Requires Python 3.0 or later
"""
import logging


__author__ = 'Stas Savinov (stanislav.savinov@dish.com)'
__copyright__ = 'Copyright (c) 2017'
__license__ = 'Apache v2.0'
__version__ = '1.0.0'
__contributors__ = ['Stas Savinov','Others']


log = logging.getLogger('usbdetectormodule')
echoHandler = logging.StreamHandler()
echoFormatter = logging.Formatter('%(levelname)-8s %(message)s')
log.addHandler(echoHandler)

# log.setLevel(logging.DEBUG)