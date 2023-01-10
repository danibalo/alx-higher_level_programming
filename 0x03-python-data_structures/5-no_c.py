#!/usr/bin/python3
def  no_c(my_string):
    new = ''
    for i in range(len(my_string) - 1):
        if my_string[i] == 'c' or my_string[i] == 'C':
            new = my_string[:i] + my_string[i + 1:]
            return new


