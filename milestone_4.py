import random


class Hangman():
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for x in self.word]
        self.num_letters = 26
        self.list_of_guesses = []

    def check_guess(self, guess: str):
        guess = str.lower(guess)
        index = 0
        if guess in self.word:
            for letter in self.word:
                if guess == letter:
                    print(f"Good guess! {guess} is in the word.")
                    self.word_guessed[index] = guess
                index += 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.num_letters -= 1
        self.list_of_guesses.append(guess)
        


    def ask_for_input(self):
        while True:
            guess = input("Guess a letter")
            if not str.alpha(guess) or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif str.lower(guess) in self.list_of_guesses:
                print("You already tried that letter!")
            else:
               self.check_guess(guess)
               self.list_of_guesses.append(guess)

test = Hangman(["apple"])
test.ask_for_input()
# %%
