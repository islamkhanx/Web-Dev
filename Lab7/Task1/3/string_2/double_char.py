# Given a string,
# return a string where for every char in the original, there are two chars.

if __name__ == '__main__':
    s = input()
    print(
        "".join([ch * 2 for ch in s])
    )
