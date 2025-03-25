# Given a number n,
# return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case
# return True if the number is less or equal to 1,
# or greater or equal to 10.

if __name__ == '__main__':
    n = int(input())
    outside_mode = input() == 'True'
    print(
        1 <= n <= 10 if not outside_mode
        else n <= 1 or n >= 10
    )
