#%%

import random


class Hangman():
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for x in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess: str):
        guess = str.lower(guess)
        index = 0
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for letter in self.word:
                if guess == letter:
                    self.word_guessed[index] = guess
                index += 1
            self.num_letters -= 1
            print(f"Word so far: {''.join(self.word_guessed)}.")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        
        
    def ask_for_input(self):
        while True:
            guess = str(input("\nGuess a letter or enter 0 for options: "))
            option_selected = False
            if guess == "0":
                option_selected, guess = self.check_state()
            if option_selected != True:
                if not str.isalpha(guess) or len(guess) != 1:
                    print("Invalid input. Please, enter a single alphabetical character or 0 for options.")
                elif str.lower(guess) in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
            break

    def check_state(self) -> tuple:
        print("\nOptions Menu:\n"
        "- Enter '1' to see the word so far.\n"
        "- Enter '2' to see which letters have already been guessed.\n"
        "- Enter '3' to see the remaining number of lives.\n"
        "- Enter '4' to give up.\n"
        "- Enter a letter to make a guess.")

        option = str(input("Option selection: "))

        # If a valid option (i.e. 1 - 4) is input, returns True so user is prompted for new input.
        # For any other input, returning False and the option input leads to the guess logic as normal.
        if option == "1":
            print(f"Word so far: {''.join(self.word_guessed)}.")
        elif option == "2":
            print(f"Letters which have been guessed: {self.list_of_guesses}")
        elif option == "3":
            print(f"Number of lives remaining: {self.num_lives}")
        elif option == "4":
            self.num_lives = 0
        else:
            return (False, option)
        return (True, option)


def play_game(word_list: list):
    game = Hangman(word_list, num_lives = 5)

    while True:
        if game.num_lives == 0:
            print("\nYou lost!"
            f"The word was '{game.word}'.")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters < 1:
            print(f"\nCongratulations. You won the game!\n"
            f"Number of guesses: {len(game.list_of_guesses)}. Best possible number of guesses: {len(set(game.word))}.")
            break

play_game(["apple", "pear", "orange", "carrot"])
# %%

