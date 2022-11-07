#%%

import random
import re
import time


class Hangman():
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

        print(f"\n{len(self.word)} letters: {''.join(self.word_guessed)}")
        print(f"You have {self.num_lives} guesses remaining.")

    def check_guess(self, guess: str):
        guess = str.lower(guess)
        index = 0
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            time.sleep(0.5)
            for letter in self.word:
                if guess == letter:
                    self.word_guessed[index] = guess
                index += 1
            self.num_letters -= 1
            print(f"Word so far: {''.join(self.word_guessed)}.")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            time.sleep(0.5)
            print(f"You have {self.num_lives} guesses left.")
        
        
    def ask_for_input(self):
        while True:
            guess = str(input("\nGuess a letter or enter 'Options' for options: "))
            option_selected = False
            if str.lower(guess) == "options":
                option_selected, guess = self.check_state()
            if option_selected == False:
                if not str.isalpha(guess) or len(guess) != 1:
                    print("Invalid input. Please, enter a single alphabetical character or 0 for options.")
                elif str.lower(guess) in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
            break

    def check_state(self) -> tuple:
        print("\n== Options Menu ==\n"
        "- Enter '1' to see the word so far.\n"
        "- Enter '2' to see which letters have already been guessed.\n"
        "- Enter '3' to see the remaining number of lives.\n"
        "- Enter '4' to see the list of possible words.\n"
        "- Enter '5' to give up.\n"
        "- Enter a letter to make a guess.\n")

        option = str(input("Option selection: "))

        # If a valid option (i.e. 1 - 4) is input, returns True so user is prompted for new input.
        # For any other input, returning False and the option input leads to the guess logic as normal.
        if option == "1":
            print(f"Word so far: {''.join(self.word_guessed)}.")
        elif option == "2":
            self.list_of_guesses.sort()
            print(f"Letters which have been guessed: {self.list_of_guesses}")
        elif option == "3":
            print(f"Number of guesses remaining: {self.num_lives}")
        elif option == "4":
            print(f"All {len(self.word_list)} possible words: {self.word_list}.")
        elif option == "5":
            self.num_lives = 0
        elif option == "Debug":
            print(f"{self.word}")
        else:
            return (False, option)
        return (True, option)


def play_game(word_list: list):
    game = Hangman(word_list, num_lives = 5)

    while True:
        time.sleep(0.5)
        if game.num_lives == 0:
            print("\nYou lost!\n"
            f"The word was '{game.word}'.")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters < 1:
            print(f"\nCongratulations. You won the game!\n"
            f"Number of guesses: {len(game.list_of_guesses)}. Best possible number of guesses: {len(set(game.word))}.")
            break

def extract_words_from_path(file_path: str) -> list:
    extracted_words = set()
    time.sleep(0.5)

    try:  
        with open(file_path, 'r', encoding = 'utf-8') as f:
            for line in f:
                clean_words = re.split("[0-9]+|\[|\]|,|\'|\"|;|\.|\?|\\n|\(|\)|-|_|\{|\}|@|#|<|>| ", f.read())
                for word in clean_words:
                    if len(word) > 4:
                        extracted_words.add(str.lower(word))
        assert len(extracted_words) > 0
        extracted_words = list(extracted_words)
        extracted_words.sort()
        print(f"Word list loaded from {file_path}.")
        return extracted_words
    except:
        # If any errors with extraction, returns default word list
        print(f"Error loading from {file_path}. Default word list used.")
        return ["apple", "banana", "carrot", "orange"] 
    

if __name__ == "__main__":
    # Hint for a file that is in the folder i.e. a file that will work
    print("Hint: Try sample.txt")
    words_for_game = extract_words_from_path(str(input("Enter file path to extract words from: ")))

    while True:
        time.sleep(0.5)
        play_game(words_for_game)
        if str.lower(input("\nEnter 'c' to play again: ")) != 'c':
            print("\nThanks for playing!")
            break
# %%

