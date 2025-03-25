# Given a string,
# return a new string made of 3 copies
# of the last 2 chars of the original string.
# The string length will be at least 2.


if __name__ == '__main__':
    s = input()
    print(s[-2:] * 3)
