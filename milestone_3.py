from curses.ascii import isalpha


while True:
    guess = input("Guess a letter")
    if str.isalpha(guess) and len(str(guess)) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.") 