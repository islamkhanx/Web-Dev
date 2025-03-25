# Given a string,
# return a "rotated left 2" version
# where the first 2 chars are moved to the end.
# The string length will be at least 2.

if __name__ == '__main__':
    s = input()
    print(s[2:] + s[:2])
