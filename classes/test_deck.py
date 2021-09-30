import unittest

from card import Card
from deck import Deck

class TestDeck(unittest.TestCase):

    def test_ace_values(self):
        two_of_hearts = Card('2', 'hearts')
        ten_of_hearts = Card('10', 'hearts')
        ace_of_hearts = Card('A', 'hearts')

        hand = Deck([ten_of_hearts, ten_of_hearts, ace_of_hearts])
        self.assertEqual(hand.check_value(), 21)

        hand = Deck([ten_of_hearts, ace_of_hearts])
        self.assertEqual(hand.check_value(), 21)

        hand = Deck([ten_of_hearts, ten_of_hearts, ace_of_hearts,
                     ace_of_hearts])
        self.assertEqual(hand.check_value(), 22)

        hand = Deck([ace_of_hearts, ace_of_hearts])
        self.assertEqual(hand.check_value(), 12)

    def test_adding_card(self):
        hand = Deck([])
        hand.add_full_deck()
        self.assertEqual(len(hand.cards), 52)

        some_cards = hand.deal(5)
        self.assertEqual(len(some_cards), 5)
        self.assertEqual(len(hand.cards), 52 - 5)

    def test_failure(self):
        hand = Deck([])
        self.assertEqual(len(hand.cards), 52)

def print_cards():
    my_deck = Deck([])

    my_deck.add_full_deck()

    for card in my_deck.cards:
        print(card)


if __name__ == '__main__':
    unittest.main()
