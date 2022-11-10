#%%

import random
import re
import time
import os



# Ideas for extensions:
# - read word_list from url
# - visual hangman. done.
# - gui
# - implement Hangman as a dataclass
# - tracking for best number of guesses for a given word
# - tracking for streaks
# - difficulty settings
# - tracking user lifetime win/loss score
# - some form of ai for guessing?


class Hangman():
    def __init__(self, word_list: list, num_lives: int = 10):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

        # Only prints hangman drawing for max lives = 10.
        self.max_lives = num_lives

        print(f"\n{len(self.word)} letters: {''.join(self.word_guessed)}")
        time.sleep(0.5)
        self.print_number_of_lives()


    def check_guess(self, guess: str) -> None:
        # Converts to lower case for easier comparison.
        guess = str.lower(guess)

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                # Changes every instance of _ for the letter to the letter.
                if guess == letter:
                    self.word_guessed[index] = guess
            # Decrements the unique letter count only once always.
            self.num_letters -=1 
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1

        time.sleep(0.5)
        self.print_word_so_far()
        time.sleep(0.5)
        self.print_number_of_lives()


    def print_word_so_far(self) -> None:
        print(f"Word so far: {''.join(self.word_guessed)}.")

    def print_number_of_lives(self) -> None:
        # Unnecessary way to print guess singular for when 1 life is remaining
        print(f"You have {self.num_lives} guess{['es',''][self.num_lives == 1]} left.")
        if self.max_lives == 10:
            self.draw_hangman(10 - self.num_lives )
        
        
    def ask_for_input(self) -> None:
        while True:
            guess = str(input("\nGuess a letter or enter 'Options' for options: "))
            option_selected = False

            # Prints options menu and prompts for user input.
            if str.lower(guess) == "options" or str.lower(guess) == "0":
                option_selected, guess = self.options_menu()
            
            # If not going to options menu, take input as normal. Check that input is valid before changing letters/number of lives.
            if option_selected == False:
                if not str.isalpha(guess) or len(guess) != 1:
                    print("Invalid input. Please, enter a single alphabetical character or 'Options' for options menu.")
                elif str.lower(guess) in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
            break

    def options_menu(self) -> tuple:
        time.sleep(1)

        print("\n== Options Menu ==\n"
        "- Enter '1' to see the word so far.\n"
        "- Enter '2' to see which letters have already been guessed.\n"
        "- Enter '3' to see the remaining number of lives.\n"
        "- Enter '4' to see the list of possible words.\n"
        "- Enter '5' to give up.\n"
        "- Enter a letter to make a guess.\n")

        option = str(input("Option selection: "))
        time.sleep(0.5)

        # If a valid option (i.e. 1 - 5) is input, returns True so user is prompted for new input.
        # For any other input, returning False and the option input leads to the guess logic as normal.
        if option == "1":
            self.print_word_so_far()
        elif option == "2":
            self.list_of_guesses.sort()
            print(f"Letters which have been guessed: {self.list_of_guesses}.")
        elif option == "3":
            self.print_number_of_lives()
        elif option == "4":
            print(f"All {len(self.word_list)} possible words: {self.word_list}.")
        elif option == "5":
            self.num_lives = 0
        elif option == "Debug":
            print(f"{self.word}")
        else:
            return (False, option)
        return (True, option)

    # Static in case you feel like drawing for different numbers, probably unnecessary
    @staticmethod
    def draw_hangman(lives_lost: int) -> None:
        try:
            assert lives_lost > 0

            time.sleep(0.5)

            # Dictionary of strings to draw the hangman, keys are the number of lives at which to start drawing the string for each line.
            hangman_dictionary_1 = {1: "", 3: "   ___"}
            hangman_dictionary_2 = {1: "", 2: "  |", 4: "  |   |"}
            hangman_dictionary_3 = {1: "", 2: "  |", 5: "  |   o", 7: "  |  _o", 8: "  |  _o_ "}
            hangman_dictionary_4 = {1: "", 2: "  |", 6: "  |   |"}
            hangman_dictionary_5 = {1: "", 2: "  |", 9: "  |  /", 10: "  |  / \\"}
            hangman_dictionary_6 = {1: "__ __", 2: "__|__"}

            # Finds highest key less than or equal to the number of lives lost
            lambda_func = lambda key: key <= lives_lost

            # list(filter(lambda_func,[x, y, z][-1])) gets the largest valid key in a dictionary which is less than the number of lives lost
            # For an using the bottom line, with 1 life lost it will print '__ __'. lambda_func returns [True, False] so filter returns [1] only.
            # Taking the -1th index returns 1.
            # For any number 2 or greater it will find '2' in the list as the last valid key in order to print '__|__'.
            # lambda_func returns [True, True] so filter returns [1, 2].
            # Taking the -1th index returns 2.
            # e.g. for lives_lost = 6, the bottom line equates to hangman_dictionary_6[2], hence selects the value from 2: '__|__ in the dictionary.
            print(f"""{hangman_dictionary_1[list(filter(lambda_func, [1, 3]))[-1]]}
{hangman_dictionary_2[list(filter(lambda_func, [1, 2, 4]))[-1]]}
{hangman_dictionary_3[list(filter(lambda_func, [1, 2, 5, 7, 8]))[-1]]}
{hangman_dictionary_4[list(filter(lambda_func, [1, 2, 6]))[-1]]}
{hangman_dictionary_5[list(filter(lambda_func, [1, 2, 9, 10]))[-1]]}
{hangman_dictionary_6[list(filter(lambda_func, [1, 2]))[-1]]}""")

        # Assertion error if no lives have been lost, skips printing a blank hangman drawing.
        except AssertionError:
            pass


def play_game(word_list: list) -> None:

    game = Hangman(word_list, 5)

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

# Could eventually extend to work for urls.
def extract_words_from_path(file_path: str, dir_name: str) -> list:
    # Is originally a set to avoid duplication.
    extracted_words = set()
    time.sleep(0.5)

    try:
        with open(dir_name + "/" + file_path, 'r', encoding = 'utf-8') as f:
            for line in f.readlines():
                # Removes special characters.
                clean_words = re.split("[0-9]+|\[|\]|,|\'|\"|;|\.|\?|\\n|\(|\)|-|_|\{|\}|@|#|<|>| ", line)
                for word in clean_words:
                    if len(word) > 4:
                        extracted_words.add(str.lower(word))
        assert len(extracted_words) > 0
        
        # Convert to list as random.choice only works with sequences apparently, guess this could be a tuple if that's faster?
        extracted_words = list(extracted_words)

        # Sorts alphabetically for options menu output.
        extracted_words.sort()

        # Confirmation message.
        print(f"Word list loaded from {file_path}.")
        return extracted_words

    except FileNotFoundError:
        # Print if file not found.
        print(f"Erorr: No file found at {file_path}. Default word list used.")
        
    except AssertionError:
        # Print if list of extracted words contains no words.
        print(f"Error: No valid words extracted from {file_path}. Default word list used.")
    
    # Return this list of words if exception is raised.
    return ["apple", "banana", "carrot", "orange"] 
    

if __name__ == "__main__":
    # Hint for a file that is in the folder i.e. a file that will work.
    dir_name = os.path.dirname(os.path.realpath(__file__))
    print(f"Current directory is: {dir_name}")

    print("Hint: Try 'sample.txt'")
    words_for_game = extract_words_from_path(str(input("Enter file name in current directory to extract words from: ")), dir_name)

    while True:
        time.sleep(0.5)

        play_game(words_for_game)

        if str.lower(input("\nEnter 'c' to play again: ")) != 'c':
            print("\nThanks for playing!")
            break
# %%

