from card import Card
from deck import Deck

my_cards = [Card('2', 'hearts'), Card('3', 'diamonds'), Card('4', 'spades')]
my_deck = Deck(my_cards)

my_deck.add_full_deck()
