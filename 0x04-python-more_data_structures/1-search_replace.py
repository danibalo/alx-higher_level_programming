#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for i in my_list:
        if search == i:
            i = replace
        new.append(i)
    return new

