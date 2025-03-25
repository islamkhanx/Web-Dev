# We want to make a row of bricks that is goal inches long.
# We have small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from given bricks.
# This is a little harder than it looks and can be done without any loops

if __name__ == '__main__':
    goal = int(input())
    small = int(input())
    big = int(input())

    print(
        ((goal % 5 <= small) and (goal // 5 <= big))
        or ((goal <= big * 5 + small) and (goal % 5 <= small))
    )
