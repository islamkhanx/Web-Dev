# Необходимо вывести  наименьшее из 4-х данных чисел.

def min4(a, b, c, d):
    return min(a, b, c, d)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(min4(a, b, c, d))
