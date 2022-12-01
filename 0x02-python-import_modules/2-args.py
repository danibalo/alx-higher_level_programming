#!/usr/bin/python3

if __name__== "__main__":
    """Print the nummber of and list of arguments."""
    import sys

    i = len(sys.argv) - 1
    if i == 0:
        print("0 arguments")
    elif i == 1:
        print("1 argument")
    else:
        print("{:d} arguments:".format(i))
    for j in range (i):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))

