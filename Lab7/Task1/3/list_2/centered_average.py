# Return the "centered" average of an array of ints,
# which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array.
# If there are multiple copies of the smallest value, ignore just one copy,
# and likewise for the largest value.
# Use int division to produce the final average.
# You may assume that the array is length 3 or more.


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print((sum(arr) - max(arr) - min(arr)) // (len(arr) - 2))
