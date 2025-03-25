
# Given 2 strings, a and b,
# return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).

if __name__ == '__main__':
    a = input()
    b = input()
    if len(a) > len(b):
        print(b + a + b)
    else:
        print(a + b + a)
