# Сначала задано число N — количество элементов в массиве
# Далее через пробел записаны элементы массива.
# Массив состоит из целых чисел.
# Необходимо количество положительных элементов в массиве.

if __name__ == '__main__':
    input()
    arr = [int(i) for i in input().split()]
    print(len([x for x in arr if x > 2 == 0]))
