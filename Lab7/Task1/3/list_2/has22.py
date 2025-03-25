# Given an array of ints,
# return True if the array contains a 2 next to a 2 somewhere.

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(
        any(
            arr[i] == 2 and arr[i + 1] == 2
            for i in range(len(arr) - 1)
        )
    )
