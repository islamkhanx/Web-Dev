if __name__ == '__main__':
    N = int(input())
    i = 2
    while N >= i:
        if N % i == 0:
            print(i)
            break
        i += 1
