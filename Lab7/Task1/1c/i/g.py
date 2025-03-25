if __name__ == '__main__':
    n = int(input())
    for i in range(2, 30_000 + 1):
        if n % i == 0:
            print(i)
            break
