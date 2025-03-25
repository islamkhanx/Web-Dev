# The parameter weekday is True if it is a weekday,
# and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation.
# Return True if we sleep in.

if __name__ == '__main__':
    weekday = input() == 'True'
    vacation = input() == 'True'
    print(not weekday or vacation)
