"""
This is a python file pep8.py. The purpose of this file is to learn how to document stuff.
This is a duplicate of main.py, but with pep8 styling.
Python files (modules) should be saved in lower snake_case.
"""

FINAL_CONST_VARIABLE = 10  # finals should be in all-caps SNAKE_CASE


class MyClass:  # class declaration should be in CamelCase
    """
    :class: myClass

    This is a general description of myClass.

    :ivar instance_var1: This is the first instance variable.
    :type instance_var1: int

    :ivar instance_var2: This is the second instance variable.
    :type instance_var2: str
    """

    def __init__(self, init1:int, init2:str):
        """
        This method initializes the instance variables of myClass

        :param init1: argument that will be assigned to instance_var1
        :type init1: int
        :param init2: argument that will be assigned to instance_var2
        :type init2: str:
        """
        self._instance_var1 = init1  # instance variables precede with _
        self._instance_var2 = init2

    def my_method(arg:int) -> (int):  # methods/functions should be in snake_case
        #define methods/functions in Python3 with def name(param:type) --> (returnType):
        '''
        This method computes a sum with arg and init1

        :param arg: what to sum with init1
        :type arg: int

        :return: sum of arg and init1
        :rtype: int

        '''
        return arg + self.init1


def my_function():
    """
    This non-OOP function prints a string and returns nothing.
    """
    this_is_a_variable = "this is a function"  # variables should be in snake_case
    print(this_is_a_variable)
