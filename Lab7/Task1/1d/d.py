# Сначала задано число N — количество элементов в массиве
# Далее через пробел записаны элементы массива.
# Массив состоит из целых чисел.
# Необходимо количество элементов массива, больших предыдущего.

if __name__ == '__main__':
    input()
    arr = [int(i) for i in input().split()]
    print(
        sum(
            [1 for i in range(1, len(arr)) if arr[i] > arr[i - 1]]
        )
    )
