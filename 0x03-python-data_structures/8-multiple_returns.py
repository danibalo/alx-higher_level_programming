#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == ():
        my_tuple = (0, None)
    else:
        my_tuple = (len(sentence), sentence[0])
        return my_tuple

