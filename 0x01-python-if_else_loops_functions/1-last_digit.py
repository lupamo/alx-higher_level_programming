#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = abs(number) % 10
sign = "-" if number < 0 else ""
if num_str == 0:
    print("Last digit of {} is {} "
          "and is 0".format(number, sign + str(num_str)))
elif num_str > 5:
    if number < 0:
        print("Last digit of {} is {}{} and is"
              " less than 6 and not 0".format(number, sign, num_str))
    else:
        print("Last digit of {} is {}{}"
              " and is greater than 5".format(number, sign, num_str))
elif num_str < 6:
    print("Last digit of {} is {}{} and"
          " is less than 6 and not 0".format(number, sign, num_str))
