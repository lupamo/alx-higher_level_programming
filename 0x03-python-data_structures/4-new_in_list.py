#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_lst = my_list[:]
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return copied_lst
    else:
        for i in copied_lst:
            copied_lst[idx] = element
            return copied_lst
