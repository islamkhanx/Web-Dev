# Given three ints, a b c,
# return True if one of b or c is "close" (differing from a by at most 1),
# while the other is "far", differing from both other values by 2 or more.


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(
        (abs(a - b) <= 1 and abs(a - c) >= 2) or
        (abs(a - c) <= 1 and abs(a - b) >= 2)
    )
