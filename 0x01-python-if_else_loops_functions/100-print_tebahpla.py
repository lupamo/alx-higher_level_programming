#!/usr/bin/python3
tebahpla = ''
for j in range(ord('z'), ord('a') - 1, -2):
    tebahpla += chr(j) + chr(j - 1 - ord('a') + ord('A'))
print("{}".format(tebahpla), end="")
