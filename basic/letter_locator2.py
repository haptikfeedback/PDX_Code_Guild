# word locator 2
list = {}

class Locator:
    def __init__(self, phrase, letter):
        self.phrase = enumerate(phrase)
        self.letter = letter

    def return_letter(self):
        for letter in self.phrase:
            if letter[1] == self.letter:
                print(letter[1])
                print(letter[0])


phrase = "applesauce"
letter = "a"

thing = Locator(phrase, letter)

thing.return_letter()