""" This module contains the Card class, which represents a playing card. """

class Card:
    values = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self, value, suit):
        if not self.check_value(value):
            print("this isn't a valid value")
        self.value = value
        self.suit = suit

    def points(self):
        if self.value in self.values:
            return self.values[self.value]
        return int(self.value)

    def check_value(self, value):
        # is it a valid face card?
        if value in self.values:
            return True

        # is it actually a number?
        try:
           number = int(value)
        except ValueError:
            return False

        # is it a sensible number?
        if number >= 2 and number <= 10:
            return True

        return False
