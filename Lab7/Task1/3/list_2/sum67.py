# Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6
# and extending to the next 7 (every 6 will be followed by at least one 7).
# Return 0 for no numbers.


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    sum_arr = 0
    not_interval = 1
    for num in arr:
        if num == 6:
            not_interval = 0
        elif num == 7:
            not_interval = 1
        sum_arr += not_interval * num

    print(sum_arr)
