import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)

class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        print(f"{self.name} has ${self.prizeMoney}\n")
        print(f"Category: {category}")
        print(f"Phrase:  {obscuredPhrase}")
        print(f"Guessed: {guessed}\n")
        return input("Guess a letter, phrase, or type 'exit' or 'pass':\n")

class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        return random.randint(1, 10) <= self.difficulty

    def getPossibleLetters(self, guessed):
        possible_letters = [letter for letter in LETTERS if letter not in guessed]
        if self.prizeMoney < VOWEL_COST:
            return [letter for lettergit  in possible_letters if letter not in VOWELS]
        return possible_letters

    def getMove(self, category, obscuredPhrase, guessed):
        possible_letters = self.getPossibleLetters(guessed)
        if not possible_letters:
            return 'pass'
        if self.smartCoinFlip():
            for letter in reversed(self.SORTED_FREQUENCIES):
                if letter in possible_letters:
                    return letter
        else:
            return random.choice(possible_letters)
