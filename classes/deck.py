"""
this module defines the Deck class, which is a collection of cards.
this collection can be shuffled, filled, dealt, etc.
"""

class Deck:
    """ see module docstring """

    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return f'Deck({self.cards}')

    def __str__(self):
        card_word = 'cards'
        if len(self.cards) == 1:
            card_word = 'card'
        return f'Deck with {len(self.cards)} {card_word}'

    # try defining a shuffle() method for our deck
