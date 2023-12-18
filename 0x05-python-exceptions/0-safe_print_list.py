#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        for j in range(x):
            print("{}".format(my_list[j], end=""), end="")
            idx += 1
    except IndexError:
        pass
    finally:
        print()
        return idx
