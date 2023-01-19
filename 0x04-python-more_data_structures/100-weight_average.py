#!usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list) != 0:
        sum1 = 0
        sum2 = 0
        for tuples in my_list:
            sum1 += tuples[0] * tuples[1]
            sum2 += tuples[1]
        return sum1 / sum2

