#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except(ZeroDivisionError, TypeError):
        c = None
    finally:
        print('Inside the result {:d}'.format(c))
    return c
