# Given an "out" string length 4, such as "<<>>", and a word,
# return a new string where the word is in the middle of the out string.

if __name__ == '__main__':
    out = input()
    word = input()
    print(out[:2] + word + out[2:])
