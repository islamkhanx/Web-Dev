# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat,
# and a boolean indicating if we are on vacation,
# return a string of the form "7:00" indicating when alarm clock should ring.
# Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
# Unless we are on vacation -- then on weekdays
# it should be "10:00" and weekends it should be "off".

if __name__ == '__main__':
    day = int(input())
    is_vacation = input() == 'True'

    if is_vacation:
        print('off' if day < 6 else '10:00')
    else:
        print('7:00' if day < 6 else '10:00')
