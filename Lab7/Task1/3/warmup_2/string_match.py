# Given 2 strings, a and b,
# return the number of the positions
# where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3,
# since the "xx", "aa", and "az" substrings appear in the same place in both.

if __name__ == '__main__':
    a = input()
    b = input()
    print(sum(
        1 for i in range(len(a) - 1)
        if a[i:i + 2] == b[i:i + 2]
    ))
