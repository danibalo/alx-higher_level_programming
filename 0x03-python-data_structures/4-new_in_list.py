#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    index_len = len(new_list) - 1
    if idx < 0 or idx > index_len:
        return my_list
    else:
        new_list[idx] = element
        return new_list
