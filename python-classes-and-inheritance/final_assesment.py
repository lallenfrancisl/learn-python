VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'


# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = list()

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)


# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def __init__(self, name):
        WOFPlayer.__init__(self, name)

    def getMove(self, category, obscuredPhrase, guessed):
        print('{} has ${}'.format(self.name, self.prizeMoney))
        print('Category: {}'.format(category))
        print('Phrase:  {}'.format(obscuredPhrase))
        print('Guessed: {}'.format(guessed))

        while True:
            word = input("Guess a letter, phrase, or type 'exit' or 'pass':")
            if word.isalpha():
                break

        return word


# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        if random.randint(1, 10) > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        result = ''

        for letter in LETTERS:
            if letter not in guessed:
                if VOWEL_COST == 250:
                    if letter not in VOWELS:
                        result = result + letter

                else:
                    result = result + letter

        return result

    def getMove(self, category, obscuredPhrase, guessed):
        guess = self.getPossibleLetters(guessed)

        if len(guess) == 0:
            return 'pass'

        if self.smartCoinFlip():
            for letter in reversed(WOFComputerPlayer.SORTED_FREQUENCIES):
                if letter in guess:
                    return letter

        else:
            return random.choice(guess)
