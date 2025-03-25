# Given two strings,
# return True if either of the strings appears at end of the other string,
# ignoring upper/lower case differences.

if __name__ == '__main__':
    a = input().lower()
    b = input().lower()
    print(a.endswith(b) or b.endswith(a))
