# Given 3 int values, a b c, return their sum.
# However, if one of the values is the same as another of the values,
# it does not count towards the sum.


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(sum({a, b, c}))
