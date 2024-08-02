#!/usr/bin/python3
""" Nqueens """
import sys



if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

y = int(sys.argv[1])


def queens(y, i=0, z=[], b=[], c=[]):
    """ seek for possible positions """
    if i < y:
        for j in range(y):
            if j not in z and i + j not in b and i - j not in c:
                yield from queens(y, i + 1, z + [j], b + [i + j], c + [i - j])
    else:
        yield z


def solve(y):
    """ solve """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(y)
