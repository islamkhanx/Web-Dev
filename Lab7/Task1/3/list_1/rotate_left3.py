# Given an array of ints length 3,
# return an array with the elements "rotated left"
# so {1, 2, 3} yields {2, 3, 1}.

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(arr[1:], arr[0])
