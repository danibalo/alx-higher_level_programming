#!usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        sum1 = 0
        sum2 = 0
        for i in my_list:
            sum1 += i[0] * i[1]
            sum2 += i[1]
        return sum1 / sum2
