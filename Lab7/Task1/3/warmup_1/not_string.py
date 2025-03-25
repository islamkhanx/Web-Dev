# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return string unchanged.

if __name__ == '__main__':
    s = input()
    print("not " + s if s[:3] != "not" else s)
