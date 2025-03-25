# Given two int values, return their sum.
# Unless the two values are the same, then return double their sum.


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(2 * (a + b) if a == b else a + b)
