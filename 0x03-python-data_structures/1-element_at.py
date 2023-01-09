#!/usr/bin/python3
def element_at(my_list, idx):
    """My function that prints lest element at given index"""
    idx_of_elements = len(my_list) - 1
    if idx < 0 or idx > idx_of_elements:
        return None
    else:
        return my_list[idx]
