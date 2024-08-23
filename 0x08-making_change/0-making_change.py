#!/usr/bin/python3
""" Making changes """

def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for d in coins:
        while check < total:
            check += d
            temp += 1
        if check == total:
            return temp
        check -= d
        temp -= 1
    return -1
