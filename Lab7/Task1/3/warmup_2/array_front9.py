# Given an array of ints,
# return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(9 in arr[:4])
