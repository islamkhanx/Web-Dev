# Return the number of times that the string "code"
# appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.
import re

if __name__ == '__main__':
    s = input()
    print(len(re.findall(r'co\we', s)))
