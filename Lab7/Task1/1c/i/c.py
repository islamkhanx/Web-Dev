# Напишите программу, вычисляющую 2 ** N

if __name__ == '__main__':
    N = int(input())
    result = 1
    for i in range(1, N + 1):
        result *= 2
    print(result)
