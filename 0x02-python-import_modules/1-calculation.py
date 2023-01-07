#!/usr/bin/python3
n = __import__('calculator_1')
if __name__ == '__main__':
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, n.add(a, b)))
    print("{} - {} = {}".format(a, b, n.sub(a, b)))
    print("{} * {} = {}".format(a, b, n.mul(a, b)))
    print("{} / {} = {}".format(a, b, n.div(a, b)))
