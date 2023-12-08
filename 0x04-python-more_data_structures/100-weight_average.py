#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == 0:
        return 0

    sum_multiple = 0
    sum_added = 0

    for x, y in my_list:
        sum_multiple += x * y

    for j in my_list:
        sum_added += j[1]
    average_w = sum_multiple / sum_added
    return average_w
