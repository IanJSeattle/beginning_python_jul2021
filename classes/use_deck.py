""" use the deck of cards """

from card import Card
from deck import Deck

card1 = Card('J', 'spades')
card2 = Card('K', 'diamonds')

my_deck = Deck([card1, card2])

print(f'this is our new deck: {my_deck}')
