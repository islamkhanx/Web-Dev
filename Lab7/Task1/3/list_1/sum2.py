# Given an array of ints, return the sum of the first 2 elements in the array.
# If the array length is less than 2, just sum up the elements that exist,
# returning 0 if the array is length 0.


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(sum(arr[:2]))
