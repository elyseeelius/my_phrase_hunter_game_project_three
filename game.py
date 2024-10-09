import random
from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ']

    def create_phrases(self):
        return [
            Phrase('Joyfulness'),
            Phrase('faithful'),
            Phrase('practice'),
            Phrase('Peace'),
            Phrase('Pythonista')
        ]

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("+" * 50)
        print("        WELCOME TO MY PHRASE HUNTER GAME")
        print("+" * 50)


    def get_guess(self):
        return input("Enter a letter: ").lower()

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f"\nNumber missed: {self.missed}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()

    def game_over(self):
        if self.missed == 5:
            print("Game Over! Better luck next time.")
        else:
            print("Congratulations! You won!")