#!/usr/bin/python3


for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i).upper() if (ord('z') - i + 1) % 2 == 0 else chr(i).lower()), end="")
