# Given a string of even length,
# return the first half.
# So the string "WooHoo" yields "Woo".

if __name__ == '__main__':
    s = input()
    print(s[:len(s) // 2])
