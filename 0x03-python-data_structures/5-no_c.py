#!/usr/bin/python3
def no_c(my_string):
    list_strings = list(my_string)
    for word in list_strings:
        if word == 'c' or word == 'C':
            list_strings.remove(word)
    return("".join(list_strings))
