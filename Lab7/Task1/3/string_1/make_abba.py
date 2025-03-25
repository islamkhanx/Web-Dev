# Given two strings, a and b,
# return the result of putting them together in the order abba, e.g.
# "Hi" and "Bye" returns "HiByeByeHi".

if __name__ == '__main__':
    a = input()
    b = input()
    print(f"{a}{b}{b}{a}")
