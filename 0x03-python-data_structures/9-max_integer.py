#!/usr/bin/python3
def max_integer(my_list=[]):
    """My function that finds maximum integer from the list"""
    max = my_list[0]
    if my_list == []:
        return None
    else:
        for integer in my_list:
            if integer > max:
                max = integer
        return max
