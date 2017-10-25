# -------------------------------------------------------------------------------------------

class NewModule(object):

    def __init__(self):
        pass

    def method_one(self, parameter_one="None", parameter_two=0):
        """
        Description: method_one
        :param parameter_one string value
        :param parameter_two int value
        :return:
        """
        print("\n F:[" + "method_one" + "] was called! \n")
        pass

    def method_two(self, name='None'):
        """
        Description: method_two
        :param name: String name
        :return: None
        """
        print("\nF:[" + "method_two" + "] was called! Parameter:" + name)

# -------------------------------------------------------------------------------------------

class NewModuleTwo(object):
    def __init__(self):
        pass
    def method_tree(self):
        """
        Description: method_tree
        :return: None
        """
        print("\n F:[" + "met_tree" + "] was called! \n")
        pass

# -------------------------------------------------------------------------------------------