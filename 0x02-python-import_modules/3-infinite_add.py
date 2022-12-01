#!/usr/bin/python3
if __name__ == "__main__":
    """ prints the result of the addition of all arguments"""
    import sys

    i = len(sys.argv) - 1
    sum = 0
    for j in range(i):
        sum = sum + int(sys.argv[j + 1])
    print("{}".format(sum))
