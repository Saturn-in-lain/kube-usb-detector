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
from usbdetectormodule.core import ListCommandGenerator
import usbdetectormodule.module

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


def retrieve_commands(additional_module_name=None):
    json = None
    if additional_module_name is not None:
        try:
            basic = ListCommandGenerator()                          # [1] Init class
            basic.set_module(additional_module_name)                # [2] Set module name to parse
            json = basic.create_json()                              # [3] Create JSON format for data
        except:
            print("[!] No module named " + additional_module_name)
    return json


def retrieve_json_description():
    '''
    Description: Retrieve JSON module description
    :return:
    '''
    basic = ListCommandGenerator()                          # [1] Init class
    basic.set_all_modules()                                 # [2] Set module names
    json = basic.create_json()                              # [3] Create JSON format for data
    return json


def call_method(class_name=None, method_name=None, **kwargs):
    '''
    Description: call_method
    :param class_name:
    :param method_name:
    :return:
    '''
    print("We calling Class:["+class_name+"] and method: " + method_name)

    if class_name is not None and method_name is not None:
        temp_class = ListCommandGenerator()._str_to_class('usbdetectormodule.module', class_name)
        inited_class = temp_class()

        intended_method = getattr(inited_class, method_name)
        retValue = intended_method(kwargs)
        return retValue

    # if kwargs.__len__() > 0:
    #     for key, value in kwargs.items():
    #         print("Params: " + key + " -> Velue: " + value)
    # else:
    #        retValue = intended_method()


# if __name__ == "__main__":
#     # retrieve_commands('module')
#     # retrieve_json_description()
#     call_method(class_name='NewModule', method_name='method_two', name="Stas")
#     pass
