"""Given an array of ints length 3, return a new array with the elements in 
reverse order, so {1, 2, 3} becomes {3, 2, 1}."""


def reverse3(num):
    first = num[0]
    second = num[1]
    third = num[2]
    # Reassign indexes
    num[0] = third
    num[2] = first
    return num
