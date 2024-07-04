#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
    - There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True- if all boxes can be opened, else return False
"""



def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, else return False
    """
    opened = set()

    for index, box in enumerate(boxes, start=0):
        if (index == 0) or (len(box) == 0):
            opened.add(index)

        for key in box:
            if (key < len(boxes)) and (key != index):
                opened.add(key)

        if len(opened) == len(boxes):
            return True
    return False
