# По данному натуральному n вычислите сумму 12+22+...+n2.

if __name__ == '__main__':
    n = int(input())
    print(sum([i * i for i in range(1, n + 1)]))
