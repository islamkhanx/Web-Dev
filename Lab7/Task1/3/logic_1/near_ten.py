# Given a non-negative number "num",
# return True if num is within 2 of a multiple of 10.

if __name__ == '__main__':
    num = int(input())
    print((10 - num % 10) <= 2)
