#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """" Prints list of integers """
    for i in range(len(my_list)):
        print("{:d}".format(int(my_list[i])))
