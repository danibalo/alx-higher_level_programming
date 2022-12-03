#!/usr/bin/python3
def element_at(my_list, idx):
    idx = 0
    for numbers in my_list:
        idx = idx + 1
    if idx < 0:
        return None
    elif idx > numbers:
        return None
    else:
        return idx - 1
