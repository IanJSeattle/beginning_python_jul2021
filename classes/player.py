""" this module represents players in our blackjack game. """

from deck import Deck

class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self._hand = Deck([])

    def __str__(self):
        return f'{self.name} has {len(self._hand.cards)} cards and {self.points} points'

    def add_card(self, card):
        self._hand.cards.append(card)
        self.points += card.points()

    def show_hand(self):
        """ print out the player's hand """
        for card in self._hand.cards:
            print(card)
        print(f'{self.points} points')
