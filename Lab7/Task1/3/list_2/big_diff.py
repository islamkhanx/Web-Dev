# Given an array length 1 or more of ints,
# return the difference between the largest and smallest values in the array.


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(max(arr) - min(arr))
