# https://github.com/walac/pyusb/blob/master/docs/tutorial.rst

import json
import inspect
import sys
import logging

"""
    [JSON FORMAT OF CLASS GENERATOR]

    Purpose of this file is to create parser for module files.
    Rules should get information about module and its methods.
    But for this better to create some automated parser with small set of rules for it creation.

"""

MODULE_NAME = 'module'
CLASS_LIST  = 'class_list'
CLASS_NAME  = 'class'
METHOD_NAME = 'method'
METHODS     = 'methods'
PARAMETERS  = 'parameters'
DESCRIPTION = 'description'

class ClassContainer(object):
    def __init__(self, name):
        self.class_name = name
        self.list_of_methods = list()

    def set_method(self, method_container):
        if method_container is not None:
            self.list_of_methods.append(method_container)


class MethodContainer(object):
    def __init__(self, name):
        self.method_name = name
        self.method_description = None
        self.method_parameters = tuple()

    def set_parameters(self, tuple_of_params):
        self.method_parameters = tuple_of_params

    def set_description(self, method_description):
        self.method_description = method_description


class ListCommandGenerator(object):

    def __init__(self):
        self.module             = None
        self.module_name        = None
        self.json_response      = None

        self.classes_in_module  = list()  # List on classes presented in module

        logging.basicConfig()
        self.logging = logging.getLogger("ListCommandGenerator")

    def set_module(self, module=None):
        """
        Method: set_class
        Description:
        :param module:
        :return:
        """
        if module is None:
            return

        if type(module) == str:
            self.module = __import__(module)
            self.module_name = module
        else:
            self.module_name = str(module)

        self.module = module

        temp = inspect.getmembers(sys.modules[module], inspect.isclass)
        self._get_list_of_classes(temp)
        self._parse()


    def _get_list_of_classes(self, list_of_tuples):
        """
        Description:
        :param list_of_tuples:
        :return:
        """
        for item in list_of_tuples:
            if type(item) is not tuple:
                self.logging.error('F:[_get_list_of_classes] Element is not tuple')
                return
            else:
                item = ClassContainer(item[0])
                self.classes_in_module.append(item)
        self.logging.debug("Classes: " + self.classes_in_module.__str__())


    def _str_to_class(self, module_name, string_name):
        """
        Description
        :param str: String name of class
        :return: Class object of requested class
        """
        return getattr(sys.modules[module_name], string_name)

    def _get_list_of_methods_in_class(self):
        """
        Description:
            Methods represented as list of tuples like:
                ('__init__', <bound method NewModule.__init__ of <module.NewModule object at 0x0000000002BD6A90>>)

        :param None
        :return:
        """
        for class_item in self.classes_in_module:

            temp_class = self._str_to_class(self.module_name, class_item.class_name)
            inited_class = temp_class()
            methods = inspect.getmembers(inited_class, predicate=inspect.ismethod)

            for method_name in methods:
                if method_name[0] != "__init__":
                    item_method = MethodContainer(method_name[0])
                    func = getattr(temp_class, item_method.method_name)
                    item_method.set_parameters(inspect.signature(func))
                    item_method.set_description(func.__doc__)
                    class_item.set_method(item_method)

    def _debug_classes(self):
        """
        Description: only debug parameters
        :return:
        """
        for class_item in self.classes_in_module:
            print("\n------------------------------------")
            print("\nClass name: " + class_item.class_name)
            print("\n------------------------------------")
            for method_item in class_item.list_of_methods:
                print("------------------------------------")
                print("\nMethod name: " + method_item.method_name)
                print("\nMethod parameters: " + str(method_item.method_parameters))
                print("\nMethod description: " + str(method_item.method_description))

    def _parse(self):
        """
        Description:
        :return:
        """
        self._get_list_of_methods_in_class()
        # self._debug_classes()


    def create_json(self):
        """
        Description: Create json class description
        :param None
        :return: json_response
        """
        data = dict()
        data[MODULE_NAME] = self.module_name

        class_list = []
        for class_item in self.classes_in_module:
            class_description = dict()
            class_description[CLASS_NAME] = class_item.class_name

            methods = dict()
            for method_item in class_item.list_of_methods:
                methods[METHOD_NAME] = method_item.method_name
                methods[PARAMETERS] = str(method_item.method_parameters)
                methods[DESCRIPTION] = str(method_item.method_description)

            class_description[METHODS] = methods
            class_list.append(class_description)

        data[CLASS_LIST] = class_list
        self.json_response = json.dumps(data)

        print(str(self.json_response))

        return self.json_response




# if __name__ == '__main__':
    # # [1] Init class
    # basic = ListCommandGenerator()
    # # [2] Set module name to parse
    # basic.set_module('module')
    # # [3] Create JSON format for data
    # basic.create_json()

