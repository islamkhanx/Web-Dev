# You and your date are trying to get a table at a restaurant.
# The parameter "you" is the stylishness of your clothes, in the range 0..10,
# and "date" is the stylishness of your date's clothes. '
# The result getting the table is encoded as 0=no, 1=maybe, 2=yes.
# If either of you is very stylish, 8 or more, then the result is 2 (yes).
# With the exception that if either of you has style of 2 or less, 0 (no).
# Otherwise the result is 1 (maybe).


if __name__ == '__main__':
    you = int(input())
    date = int(input())
    print(
        2 if you >= 8 or date >= 8
        else 1 if you <= 2 or date <= 2
        else 0
    )
