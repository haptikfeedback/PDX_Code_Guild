from card import Card
from random import shuffle


class Deck:
    NAME_VALUE = {
        'Ace': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }
    SUIT = [
        "Clubs",
        "Diamonds",
        "Hearts",
        "Spades"
    ]

    def __init__(self, num_decks=6):
        self.deck = self.create_deck(num_decks)
        self.shuffle_deck()

    def create_deck(self, number_decks):
        temp_deck = []
        for n in range(number_decks):
            for s in self.SUIT:
                for r, v in self.NAME_VALUE.items():
                    temp_deck.append(Card(s, r, v))
        return temp_deck

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


if __name__ == '__main__':
    d = Deck()
    print(d.deck)
