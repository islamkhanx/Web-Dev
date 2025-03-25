# Given 2 ints, a and b, return their sum.
# However, sums in the range 10..19 inclusive,
# are forbidden, so in that case just return 20.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if 10 <= a + b <= 19:
        print(20)
    else:
        print(a + b)
