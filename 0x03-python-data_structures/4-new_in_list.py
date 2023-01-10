#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    index_len = len(my_list) - 1
    new_my_list = my_list.copy()
    if idx < 0 or idx > index_len:
        return my_list
    else:
        new_my_list[idx] = element
        return new_my_list
