#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == 0:
        return 0

    mutiplied = sum(x * y for x, y in my_list)
    added = sum(j[1] for j in my_list)
    average_w = mutiplied / added
    return average_w
