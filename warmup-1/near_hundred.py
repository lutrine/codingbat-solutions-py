"""Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) 
computes the absolute value of a number."""


def near_hundred(n):
    return (90 <= n <= 110) or (190 <= n <= 210)
