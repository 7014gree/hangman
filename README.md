# Hangman

## Milestone 2
- Code imports the package random to randomly select a word from a list
- Code takes user input with prompt for a single letter and checks that the input was valid


## Milestone 3
- Code checks if the user input is in the word 'apple'
- Code now uses functions for taking user input and checking the user input against the word

## Milestone 4
- Creates Hangman class
- Adds logic for checking if a guess was correct or not and check for letters which have already been guessed
- Adds logic for dealing with correct and incorrect guesses (i.e. revealing letters, recording guesses made so far, reducing lives on incorrect guesses)

## Milestone 5
- Adds play_game method for to initialise game and keep track of the state of the game (win, loss, take input from user for next turn)
- As an extension, added an options menu to show the player further information about the state of the game (number of lives, what the word looks like after guesses made so far, letters which have already been guessed, an option to give up)
- Modified print statements to give more information to the user, such as how many guesses it took upon a win or what the word was upon a loss.

## Extensions
- Added functionality to populate the word list from a given file path. Uses a regular expression to remove special characters.
- Future tasks: implement Hangman as a data class, populate the world list using a url.