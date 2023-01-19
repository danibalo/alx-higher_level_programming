#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dictionary_copy = dict(a_dictionary)
    for i in a_dictionary_copy:
        if a_dictionary_copy[i] == value:
            del a_dictionary[i]
    return a_dictionary
