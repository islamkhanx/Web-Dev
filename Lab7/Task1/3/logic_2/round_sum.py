# For this problem, we'll round an int value up to the next multiple of 10
# if its rightmost digit is 5 or more, so 15 rounds up to 20.
# Alternately, round down to the previous multiple of 10
# if its rightmost digit is less than 5, so 12 rounds down to 10.
# Given 3 ints, a b c, return the sum of their rounded values.
# To avoid code repetition, write a separate helper "def round10(num):".
# Write the helper entirely below and at the same indent level as round_sum().

def round10(num):
    return (num + 5) // 10 * 10


def round_sum(*args):
    return sum(map(round10, args))


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(round_sum(a, b, c))
