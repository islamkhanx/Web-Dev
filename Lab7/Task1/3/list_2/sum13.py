# Return the sum of the numbers in the array,
# returning 0 for an empty array.
# Except the number 13 is very unlucky,
# so it does not count and numbers that come immediately after a 13 also.


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(
        sum(
            arr[i] for i in range(len(arr))
            if arr[i] != 13 and (i == 0 or arr[i - 1] != 13)
        )
    )
