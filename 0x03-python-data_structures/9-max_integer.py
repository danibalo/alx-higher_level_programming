#!/usr/bin/python3
def max_integer(my_list=[]):
    """My function that finds maximum integer from the list"""
    max = my_list[0]
    if len(my_list) == 0:
        return None
    else:
        for number in my_list:
            if number > max:
                max = number
        return max
