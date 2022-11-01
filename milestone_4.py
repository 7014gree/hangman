import random


class Hangman():
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for x in self.word]
        self.num_letters = 0
        self.list_of_guesses = []