"""
Custom implementation of the game wordle
"""

database = ["PHONE"] #Here it will select the words from
LIMIT = len(database)

class Wordle:
    "Wordle game class"

    def __init__(self, max_attempts, word):
        self.word = word
        self.size = len(self.word)
        self.attempts = []
        self.num_attempts = 0
        self.max_attempts = max_attempts
        self.won = False
        
    def guess_word(self, guess):
        #Only accept same-sized words
        if len(guess) != self.size:
            return "Unvalid attempt"

        #Only allow certain attempts
        if(self.num_attempts >= self.max_attempts):
            return "This game is already over"
        
        #Evaluate green matches
        matches = []
        for i,char in enumerate(guess):
            matches.append('1' if char == self.word[i] else '0')
        
        #See if player won
        if matches == ['1'] * self.size:
            self.won = True
            return "Congratulations. You won"

        self.attempts.append(guess)
        self.num_attempts += 1

        #Returns matching map
        return ''.join(matches)

        
