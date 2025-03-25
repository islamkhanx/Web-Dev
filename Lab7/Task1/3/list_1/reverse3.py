# Given an array of ints length 3,
# return a new array with the elements in reverse order,
# so {1, 2, 3} becomes {3, 2, 1}.

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(arr[::-1])
