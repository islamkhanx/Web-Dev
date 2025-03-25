# The squirrels in Palo Alto spend most of the day playing.
# In particular, they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90.
# Given an int temperature and a boolean is_summer,
# return True if the squirrels play and False otherwise.

if __name__ == '__main__':
    temperature = int(input())
    is_summer = input() == 'True'
    print(60 <= temperature <= (100 if is_summer else 90))
