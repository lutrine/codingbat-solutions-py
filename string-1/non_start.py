"""Given 2 strings, return their concatenation, except omit the first char of 
each. The strings will be at least length 1."""


def non_start(a, b):
    start = a[1:]
    end = b[1:]
    return start + end
