# We have a loud talking parrot.
# The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if parrot is talking and the hour is before 7 or after 20.
# Return True if we are in trouble.

if __name__ == '__main__':
    hour = int(input())
    print(hour < 7 or hour > 20)
