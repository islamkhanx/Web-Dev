# Given 2 arrays of ints, a and b,
# return True if they have the same first element
# or they have the same last element.
# Both arrays will be length 1 or more.


if __name__ == '__main__':
    arr1 = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]
    print(arr1[0] == arr2[0] or arr1[-1] == arr2[-1])
