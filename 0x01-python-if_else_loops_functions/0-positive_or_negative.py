#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    print("{} is positive\n".format(number))
elif number == 0:
    print("{} is zero\n".format(number))
elif number < 0:
    print("{} is negative\n".format(number))
