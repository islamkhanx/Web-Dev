# Given an int n, return True if it is within 10 of 100 or 200.
#  Note: abs(num) computes the absolute value of a number.

if __name__ == "__main__":
    n = int(input())
    print(abs(n - 100) <= 10 or abs(n - 200) <= 10)
