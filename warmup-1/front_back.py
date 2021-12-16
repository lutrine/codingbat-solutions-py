"""Given a string, return a new string where the first and last chars have been 
exchanged."""


def front_back(str):
    if len(str) <= 1:
        return str

    # slices the first and last character
    mid = str[1:-1]

    # last + mid + first
    return str[len(str) - 1] + mid + str[0]
