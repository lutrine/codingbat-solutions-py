"""Given an array of ints length 3, return an array with the elements "rotated 
left" so {1, 2, 3} yields {2, 3, 1}."""


def rotate_left3(num):
    first = num[0]
    second = num[1]
    third = num[2]
    # Reassign indexes
    num[0] = second
    num[1] = third
    num[2] = first
    return num
