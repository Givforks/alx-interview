#!/usr/bin/python3
"""
Checks if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Checks if a given dataset represents utf8."""
    q, mask1, mask2 = 0, 1 << 7, 1 << 6

    for num in data:
        mask = 1 << 7
        if q == 0:
            while mask & num:
                q += 1
                mask = mask >> 1
                """encoding iterations""" 
            if q == 0:
                continue
            if q == 1 or q > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        q -= 1
    return q == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105,
            115, 32, 99, 111, 111, 108, 33
            ]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
