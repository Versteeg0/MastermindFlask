from random import randint


class Game:
    def __init__(self):
        self.colors = []
        self.createColorArray()
        self.code = []
        self.guesses = {}
        self.checklist = {}
        self.times_guessed = 0
        self.color_amount = 0
        self.box_amount = 0
        self.godmode = False

    def createCode(self, multiple_colors):
        self.code.clear()
        if multiple_colors == "Ja":
            for i in range(self.box_amount):
                self.code.append(self.colors[randint(0, self.color_amount - 1)])
        else:
            colors = self.box_amount
            numbers = []
            while colors > 0:
                number = randint(0, self.color_amount - 1)
                if number not in numbers:
                    self.code.append(self.colors[number])
                    numbers.append(number)
                    colors = colors - 1
        self.guesses.clear()
        self.times_guessed = 0

    def addGuess(self, guess):
        self.times_guessed = self.times_guessed + 1
        self.guesses[self.times_guessed] = guess
        return self.checkCode(guess)

    def addCheck(self, guessed, in_code):
        filled = 0
        checklist = []
        if guessed > 0:
            for i in range(guessed):
                checklist.append("red")
                filled = filled + 1
        if in_code > 0:
            for i in range(in_code):
                checklist.append("white")
                filled = filled + 1
        while filled < self.box_amount:
            checklist.append("gray")
            filled = filled + 1
        self.checklist[self.times_guessed] = checklist
        return self.checklist

    def setColorAmount(self, amount):
        self.color_amount = amount

    def setBoxAmount(self, amount):
        self.box_amount = amount

    def setGodmode(self, godmode):
        if godmode == 'Ja':
            self.godmode = True
        else:
            self.godmode = False

    def checkCode(self, guess):
        correct = 0
        in_code = 0
        code = self.code.copy()
        guess = guess.copy()
        for i in range(self.box_amount):
            if guess[i] == code[i]:
                correct = correct + 1
                code[i] = "guessed"
                guess[i] = ""
        for i in range(self.box_amount):
            if guess[i] in code:
                index = code.index(guess[i])
                code[index] = "guessed"
                in_code = in_code + 1
        return correct, in_code

    def getCode(self):
        return self.code

    def getGuesses(self):
        return self.guesses

    def getTimesGuessed(self):
        return self.times_guessed

    def getBoxAmount(self):
        return self.box_amount

    def getColors(self):
        colors = []
        for i in range(self.color_amount):
            colors.append(self.colors[i])
        return colors

    def getGodmode(self):
        return self.godmode

    def createColorArray(self):
        self.colors.append("red")
        self.colors.append("blue")
        self.colors.append("green")
        self.colors.append("yellow")
        self.colors.append("purple")
        self.colors.append("pink")
        self.colors.append("black")
        self.colors.append("white")
        self.colors.append("orange")
        self.colors.append("brown")
