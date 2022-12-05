#!/usr/bin/python3
def print_reversed_list_integer(my_list = []):
    i = 0
    for numbers in my_list:
        i = i + 1
        j = i - 1
    while j  >= 0:
        print("{}".format(my_list[j]))
        j = j - 1

