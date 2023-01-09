#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    index_len = len(my_list) - 1
    while(index_len >= 0):
        print("{:d}".format(my_list[index_len]))
        index_len -= 1
