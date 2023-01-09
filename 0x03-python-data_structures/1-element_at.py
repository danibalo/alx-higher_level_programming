#!/usr/bin/python3
def element_at(my_list, idx):
    """My function that prints lest element at given index"""
    number_of_element = len(my_list)
    if idx < 0 or idx > number_of_element:
        return None
    else:
        return my_list[idx]
