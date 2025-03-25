# Given an array of ints,
# return True if 6 appears as either the first or last element in the array.
# The array will be length 1 or more.


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(arr[0] == 6 or arr[-1] == 6)
