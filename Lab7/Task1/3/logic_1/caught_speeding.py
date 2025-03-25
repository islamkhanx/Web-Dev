# You are driving a little too fast, and a police officer stops you.
# Write code to compute the result,
# encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
# If speed is 60 or less, the result is 0.
# If speed is between 61 and 80 inclusive, the result is 1.
# If speed is 81 or more, the result is 2.
# Unless it is your birthday -- your speed can be 5 higher in all cases.


if __name__ == '__main__':
    speed = int(input())
    is_birthday = input() == 'True'
    speed -= 5 if is_birthday else 0
    print(
        0 if speed <= 60
        else 1 if speed <= 80
        else 2
    )
