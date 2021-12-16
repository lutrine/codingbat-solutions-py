"""Given a string, return a new string where "not " has been added to the 
front. However, if the string already begins with "not", return the string 
unchanged. """


def not_string(str):
    # check if str both
    # more than or equal to three, and
    # first three characters are "not"
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str
