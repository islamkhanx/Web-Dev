# Given an int array length 2, return True if it contains a 2 or a 3.

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(2 in arr or 3 in arr)
