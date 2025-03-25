# We have two monkeys, a and b,
# and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling.
# Return True if we are in trouble.

if __name__ == '__main__':
    a_smile = input() == 'True'
    b_smile = input() == 'True'
    print(a_smile == b_smile)
