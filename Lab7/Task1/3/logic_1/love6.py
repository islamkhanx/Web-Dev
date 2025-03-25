
# The number 6 is a truly great number.
# Given two int values, a and b,
# return True if either one is 6.
# Or if their sum or difference is 6.

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6)
