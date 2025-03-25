# Given an int n,
# return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

if __name__ == '__main__':
    n = int(input())
    print(
        abs(n - 21) if n <= 21
        else 2 * abs(n - 21)
    )
