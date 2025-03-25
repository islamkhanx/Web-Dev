# Return True if the given string contains an appearance of "xyz"
# where the xyz is not directly preceeded by a period (.).
# So "xxyz" counts but "x.xyz" does not.
import re

if __name__ == '__main__':
    s = input()
    print(bool(re.search(r'(?<!\.)xyz', s)))
