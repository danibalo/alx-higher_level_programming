#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length_of_idx = len(my_list)
    if idx < 0 or idx > length_of_idx:
        return my_list
    else:
        my_list[idx] = element
        return my_list
