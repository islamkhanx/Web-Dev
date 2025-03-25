# We want make a package of goal kilos of chocolate.
# We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use,
# assuming we always use big bars before small bars.
# Return -1 if it can't be done.

if __name__ == '__main__':
    goal = int(input())
    small = int(input())
    big = int(input())

    print(
        -1 if goal > big * 5 + small
        else goal % 5 if goal % 5 <= big
        else goal - big * 5
    )
