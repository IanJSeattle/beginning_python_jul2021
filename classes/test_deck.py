from pprint import pprint as pp

from card import Card
from deck import Deck

#my_cards = [Card('2', 'hearts'), Card('3', 'diamonds'), Card('4', 'spades')]
#my_deck = Deck(my_cards)
my_deck = Deck([])

my_deck.add_full_deck()

for card in my_deck.cards:
    print(card)

#assert Card('2', 'hearts') in my_deck.cards
#assert Card('10', 'hearts') in my_deck.cards
#assert Card('5', 'spades') in my_deck.cards

#print('all tests passed')


