"""
This is a python file main.py. The purpose of this file is to learn how to document stuff.
"""


class myClass():
    """
    :class: myClass

    This is a general description of myClass.

    :ivar instance_var1: This is the first instance variable.
    :type instance_var1: int

    :ivar instance_var2: This is the second instance variable.
    :type instance_var2: str
    """

    def __init__(self, init1, init2):
        """
        This method initializes the instance variables of myClass

        :param init1: argument that will be assigned to instance_var1
        :type init1: int
        :param init2: argument that will be assigned to instance_var2
        :type init2: str:
        """
        self.instance_var1 = init1
        self.instance_var2 = init2

    def myMethod(arg):
        '''
        This method computes a sum with arg and init1

        :param arg: what to sum with init1
        :type arg: int

        :return: sum of arg and init1
        :rtype: int

        '''
        return arg + self.init1


def myFunction():
    """
    This non-OOP function prints a string and returns nothing.
    """
    print("this is a function")
