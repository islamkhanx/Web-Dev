# Given a string,
# return a new string where the first and last chars have been exchanged.

if __name__ == '__main__':
    s = input()
    print(s[-1] + s[1:-1] + s[0])
