#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if n < 0:
            return str
        return str[:n] + str[n + 1:]
