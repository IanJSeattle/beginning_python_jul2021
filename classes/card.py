""" This module contains the Card class, which represents a playing card. """

class CardSenseError(Exception):
    """ this error is thrown when the card doesn't make sense """

class Card:
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = [str(num) for num in numbers]
    values = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    suits = ['hearts', 'diamonds', 'clubs', 'spades']

    def __init__(self, value, suit):
        if not self.validate_value(value):
            raise CardSenseError(f"{value} isn't a valid value")
        if suit not in self.suits:
            raise CardSenseError(f'{suit} is not a valid suit')
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"Card('{self.value}', '{self.suit}')"

    def __str__(self):
        values = {'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'}
        if self.value in values:
            return f'{values[self.value].title()} of {self.suit}'
        return f'{self.value} of {self.suit}'

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other):
        return self.points() < other.points()

    def points(self):
        if self.value in self.values:
            return self.values[self.value]
        return int(self.value)

    def validate_value(self, value):
        # is it a valid face card?
        if value in self.values:
            return True

        # is it a string like it should be?
        if not isinstance(value, str):
            return False

        # is it actually a number?
        try:
           number = int(value)
        except ValueError:
            return False

        # is it a sensible number?
        if number >= 2 and number <= 10:
            return True

        return False
