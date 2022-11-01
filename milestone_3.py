def ask_for_input():
    while True:
        guess = input("Guess a letter")
        if str.isalpha(guess) and len(str(guess)) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)

word = "apple"

def check_guess(guess: str):
    guess = str.lower(guess)
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()