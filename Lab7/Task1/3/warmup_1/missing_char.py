# Given a non-empty string and an int n,
# return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string.

if __name__ == '__main__':
    s = input()
    n = int(input())
    print(s[:n] + s[n + 1:])
