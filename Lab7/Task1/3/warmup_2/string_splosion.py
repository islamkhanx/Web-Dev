# Given a non-empty string like "Code" return a string like "CCoCodCode".

if __name__ == '__main__':
    s = input()
    print(
        "".join([s[:i + 1] for i in range(len(s))])
    )
