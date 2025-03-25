# Given a string,
# return the string made of its first two chars,
# so the String "Hello" yields "He".
# If the string is shorter than length 2,
# return whatever there is, so "X" yields "X",
# and the empty string "" yields the empty string "".

if __name__ == '__main__':
    s = input()
    print(s[:2])
