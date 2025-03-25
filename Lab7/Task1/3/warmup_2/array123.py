# Given an array of ints,
# return True if the sequence of numbers 1, 2, 3 appears in the array.

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print("123" in "".join(map(str, arr)))
