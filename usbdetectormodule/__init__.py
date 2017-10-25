# -*- coding: utf-8 -*-
#
# vim: sw=2 ts=2 sts=2
#
# Copyright 2017 Stas Savinov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from usbdetectormodule import *

"""
Module: usbdetectormodule
Description:
Requires: Python 2.6 or later
"""
__author__ = 'Stas Savinov'
__email__ = 'stanislav.savinov@dish.com'
__copyright__ = 'Copyright (c) 2017 Stas Savinovr'
__license__ = 'Apache License 2.0'
__version__ = '0.1'
__url__ = 'https://github.com/Saturn-in-lain/kube-usb-detector'
__description__ = 'Demo project as proof of concept'
__download_url__ = 'git+https://github.com/Saturn-in-lain/kube-usb-detector'

# -------------------------------------------------------------------------------------------------------------------
# Here will be module logic concentrated

# [1] Must be general list of commands generator

# -------------------------------------------------------------------------------------------------------------------


def _retrieve_commands():
    basic = ListCommandGenerator()      # [1] Init class
    basic.set_module('module')          # [2] Set module name to parse
    json = basic.create_json()          # [3] Create JSON format for data
    return json


def call_method(class_name='default', method_name='default'):
    '''
    Description: call_method
    :param class_name:
    :param method_name:
    :return:
    '''
    print("We called " + class_name + " and method: " + method_name)
    pass

# if __name__ == "__main__":
#     _retrieve_commands()
#     pass
