# Given an array of ints,
# return True if the array is length 1 or more,
# and the first element and the last element are equal.
# The array will be length 1 or more.


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    if arr:
        print(arr[0] == arr[-1])
