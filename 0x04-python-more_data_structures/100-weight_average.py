#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_multiple = 0
    sum_added = 0

    if not my_list:
        return 0
    else:
        for x, y in my_list:
            sum_multiple += x * y

        for j in my_list:
            sum_added += j[1]
    average_w = sum_multiple / sum_added
    return average_w
