def xor(a, b):
    return int((a and not b) or (not a and b))


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(xor(a, b))
