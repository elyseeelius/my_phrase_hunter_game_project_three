class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        display_phrase = ''
        for letter in self.phrase:
            if letter in guesses:
                display_phrase += f'{letter} '
            else:
                display_phrase += '_ '
        print(display_phrase.strip())

    def check_guess(self, guess):
        return guess in self.phrase

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses and letter != ' ':
                return False
        return True