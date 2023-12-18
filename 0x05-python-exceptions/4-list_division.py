#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    for j in range(list_length):
        try:
            div.append(my_list_1[j] / my_list_2[j])
        except TypeError:
            print("wrong type")
            div.append(0)
        except ZeroDivisionError:
            print("division by 0")
            div.append(0)
        except IndexError:
            print("out of range")
            div.append(0)
    return div