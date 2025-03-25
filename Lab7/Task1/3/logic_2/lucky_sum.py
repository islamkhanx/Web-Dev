# Given 3 int values, a b c, return their sum.
# However, if one of the values is 13 then it does not count towards the sum
# and values to its right do not count.
# So for example, if b is 13, then both b and c do not count.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(
        0 if a == 13
        else a if b == 13
        else a + b if c == 13
        else a + b + c
    )
