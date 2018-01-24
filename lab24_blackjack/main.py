from deck import Deck
from hand import Hand
import time


class BlackJack:
    def __init__(self, shoe_size=1):
        self.deck = Deck(shoe_size)
        self.players = self.setup_players()
        self.dealer = Hand('Dealer')

    def setup_players(self):
        plrs = []
        while True:
            try:
                q = int(input('How many players are there?: '))
                break
            except ValueError:
                print('Please enter a base 10 number.')
        for i in range(q):
            player_name = input('What is the name of player {}?: '.format(i + 1))
            plrs.append(Hand(player_name))
        return plrs

    def deal_round(self):
        for i in range(2):
            for p in self.players:
                p.take(self.deck.deal_card())
            self.dealer.take(self.deck.deal_card())

    def play_round(self):
        self.deal_round()
        for p in self.players:
            while p.score() <= 21:
                p.display_hand()
                q = input('Would you like to (H)it or (S)tay?: ').lower()
                if q == 'h':
                    p.take(self.deck.deal_card())
                elif q == 's':
                    break
            else:
                if p.score() > 21:
                    p.display_hand()
        else:
            self.dealer.display_hand()
            d_score = self.dealer.score()
            while d_score < 17:
                self.dealer.take(self.deck.deal_card())
                self.dealer.display_hand()
                d_score = self.dealer.score()
                time.sleep(1)

    def clear_hands(self):
        for p in self.players:
            p.clear()
        self.dealer.clear()

    def score_game(self):
        winner = self.dealer
        score = self.dealer.score() if self.dealer.score() <= 21 else 0
        for p in self.players:
            if 22 > p.score() > score:
                score = p.score()
                winner = p
        return winner

    def game(self):
        while True:
            self.play_round()
            print('{} wins!'.format(self.score_game().name))
            self.clear_hands()
            q = input("Would you like to play again?: ").lower()
            if 'n' in q:
                quit()


if __name__ == '__main__':
    game = BlackJack()
    game.game()
