# -------------------------------------------------------------------------------------------

class NewModule(object):

    def __init__(self):
        pass

    def method_one(self, kwargs):
        """
        Description: method_one
        :param kwargs: is general dictionary
         * parameter_one string value
         * parameter_two int value
        :return:
        """
        print("\n F:[" + "method_one" + "] was called! \n")
        return True

    def method_two(self, kwargs):
        """
        Description: method_two
        :param kwargs: is general dictionary
            - name - as String value
        :return: None
        """
        print("\nF:[" + "method_two" + "] --> START")

        if kwargs.__len__() > 0:
            for key, value in kwargs.items():

                if str(key) == 'name':
                    if value is None:
                        return False
                    else:
                        print("\nF:[" + "method_two" + "] was called! Parameter:" + value)
        return True



# -------------------------------------------------------------------------------------------

class NewModuleTwo(object):
    def __init__(self):
        pass
    def method_tree(sel,kwargs):
        """
        Description: method_tree
        :param kwargs: is general dictionary
        :return: None
        """
        print("\n F:[" + "met_tree" + "] was called! \n")
        return True

# -------------------------------------------------------------------------------------------