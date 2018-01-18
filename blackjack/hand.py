class Hand:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_score = 0

    def take(self, card):
        self.hand.append(card)

    def clear(self):
        self.hand = []

    def display_hand(self):
        print()
        print('*' * 20)
        print(self.name)
        print(self.hand)
        print(self.score())
        print('*' * 20)

    def score(self):
        total = 0
        ace = False
        for c in self.hand:
            if c.value == 1:
                ace = True
            total += c.value
        if ace and total <= 11:
            total += 10
        self.hand_score = total
        return total

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


# if __name__ == '__main__':
#     from card import Card
#
#     ten = Card('Hearts', '10', 10)
#     five = Card('Hearts', '5', 5)
#     ace = Card('Hearts', 'Ace', 1)
#     king = Card('Hearts', 'King', 10)
#     chris = Hand('Chris')
#     chris.take(ten)
#     chris.take(five)
#     print(chris.score())
#
#     katie = Hand('Katie')
#     katie.take(ace)
#     katie.take(king)
#     print(katie.score())
