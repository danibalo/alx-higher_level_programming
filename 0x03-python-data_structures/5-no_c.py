#!/usr/bin/python3
def  no_c(my_string):
    index_len = len(my_string) - 1
    for i in range(index_len):
        if my_string[i] == 'c' or my_string[i] == 'C':
            return my_string[:i] + my_string[i + 1:]


