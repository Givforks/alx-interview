#!/usr/bin/python3
"""consider if given data set reps valid UTF-8 encoding.
"""


def validUTF8(data):
"""consider if given data set reps valid UTF-8 encoding.
"""
    s = 0
    t = 1 << 6
    for n in data:
        mask = 1 << 7
        if s == 0:
            while n & mask:
                s += 1
                mask = mask >> 1
            if s > 4 or s == 1:
                return False
            if s == 0:
                continue
        else:
            if not (n & mask and not (n & t)):
                return False
        s -= 1
    return s == 0
