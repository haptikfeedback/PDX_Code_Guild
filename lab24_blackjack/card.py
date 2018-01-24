class Card:
    def __init__(self, suit, rank, value=0):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        if self.rank == '10':
            return '10 of {}'.format(self.suit[0:9])
        return '{} of {}'.format(self.rank[0:9], self.suit[0:9])


if __name__ == '__main__':
    ace = Card('Hearts', 'Ace', 1)
    print(ace)
    print([ace])
    print(ace.suit)
    print(ace.rank)
    print(ace.value)
