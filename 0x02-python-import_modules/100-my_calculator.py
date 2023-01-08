#!/usr/bin/python3
if __name__ == '__main__':

    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
         print('Usage: ./100-my_calculator.py <a> <operator> <b>')
         exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
            sys.exit(0)
        elif operator == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            sys.exit(0)
        elif operator == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            sys.exit(0)
        elif operator == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
            sys.exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
