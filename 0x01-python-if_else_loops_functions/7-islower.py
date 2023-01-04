#!/usr/bin/python3
def islower(c):
    '''a function that checks for lowercase character.'''
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False
