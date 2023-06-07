#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        n = ord(str[i])
        if n >= ord("a") and n <= ord("z"):
            n -= 32
        print("{}".format(chr(n)), end="")
    print("")
