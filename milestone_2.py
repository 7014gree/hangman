from curses.ascii import isalpha
import random


word_list = ["banana", "apple", "pear", "lemon", "lime"]

word = random.choice(word_list)

print(word)

guess = input(f'Enter a single letter')

if str.isalpha(guess) and len(str(guess)) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")