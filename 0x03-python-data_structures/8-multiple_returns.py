#!/usr/bin/python3
def multiple_returns(sentence):
    """"My function for tuple of length of string and its 1st character"""
    tuple_ = ()
    if len(sentence) != 0:
        tuple_ = (len(sentence), sentence[0])
    else:
        tuple_ = (len(sentence), None)
    return tuple_
