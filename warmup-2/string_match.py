"""Given 2 strings, a and b, return the number of the positions where they 
contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since 
the "xx", "aa", and "az" substrings appear in the same place in both strings."""


def string_match(a, b):
    short = ""
    if len(a) > len(b):
        short = b
    else:
        short = a

    count = 0
    for i in range(len(short) - 1):
        if a[i] == b[i] and a[i + 1] == b[i + 1]:
            count += 1
    return count
