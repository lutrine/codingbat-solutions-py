"""Given a string, return a new string made of every other char starting with 
sthe first, so "Hello" yields "Hlo"."""


def string_bits(str):
    result = ""  # placeholder
    for i in range(len(str)):  # scans each letter
        if i % 2 == 0:  # if the letter is even index
            result = result + str[i]  # add to result
    return result
