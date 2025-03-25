# Given 2 int values,
# return True if one is negative and one is positive.
# Except if the parameter "negative" is True,
# then return True only if both are negative.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    negative = input() == 'True'
    print((a < 0 and b > 0 and not negative) or (negative and a < 0 and b < 0))
