# Выведите все точные квадраты натуральных чисел,
# не превосходящие данного числа N.

if __name__ == '__main__':
    N = int(input())
    n = 0
    while N >= n * n:
        print(n * n)
        n += 1
