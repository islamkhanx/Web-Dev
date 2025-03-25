# When squirrels get together for a party, they like to have cigars.
# Squirrel party is successful when the number of cigars is between 40 and 60.
# Unless it is the weekend, in which case there is no upper bound.
# Return True if the party with  is successful, or False otherwise.

if __name__ == '__main__':
    cigars = int(input())
    is_weekend = input() == 'True'
    print(cigars >= 40 and (not is_weekend or cigars <= 60))
