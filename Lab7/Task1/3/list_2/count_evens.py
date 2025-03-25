# Return the number of even ints in the given array.
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(sum([1 - i % 2 for i in arr]))
