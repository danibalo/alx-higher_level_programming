#usr/bin/python3
def max_integer(my_list=[]):
    """My function that finds maximum integer from the list"""
    idx_len = len(my_list)
    for i in range(idx_len):
        if my_list[i] > my_list[i + 1]:
            return my_list[i]
        else:
            return my_list[i + 1]
