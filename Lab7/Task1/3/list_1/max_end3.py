# Given an array of ints length 3,
# figure out which is larger, the first or last element in the array,
# and set all the other elements to be that value. Return the changed array.

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print([arr[0]] * 3 if arr[0] > arr[-1] else [arr[-1]] * 3)
