"""
this module defines the Deck class, which is a collection of cards.
this collection can be shuffled, filled, dealt, etc.
"""

import random
from card import Card

class Deck:
    """ see module docstring """

    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return f'Deck({self.cards})'

    def __str__(self):
        card_word = 'cards'
        if len(self.cards) == 1:
            card_word = 'card'
        return f'Deck with {len(self.cards)} {card_word}'

    def shuffle(self):
        """ shuffle the deck to ensure randomness """
        random.shuffle(self.cards)

    def deal(self, number=1): # ignore "number" for the moment
        """ deal out the specified number of cards """
        if len(self.cards) == 0:
            return []
        cards_to_deal = []
        for i in range(number):
            cards_to_deal.append(self.cards.pop(0))
        return cards_to_deal

    def add_full_deck(self):
        """ add a full 52-card set of cards to this deck """
        all_values = Card.numbers + list(Card.values.keys())
        # HOMEWORK FOR 9/16:
        #
        # all_values now contains a valid list of all values.
        # using a pair of for loops (one inside the other) and the
        # all_values variable, and Card.suits attribute, add a full set
        # of cards to self.cards inside this method.
        #
        # in a separate file, create a new Deck object with an empty
        # list of cards, call add_full_deck() on that deck, and check
        # to make sure you have all the cards you would expect.
        for value in all_values:
            for suit in Card.suits:
                self.cards.append(Card(value, suit))

    def check_value(self):
        """ return the number of points this hand is worth """
        total = 0
        for card in self.cards:
            total += card.points()
        return total
