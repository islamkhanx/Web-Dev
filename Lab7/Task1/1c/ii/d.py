if __name__ == '__main__':
    N = int(input())
    i = 0
    while N >= 2 ** i:
        if N == 2 ** i:
            print("YES")
    else:
        print("NO")
