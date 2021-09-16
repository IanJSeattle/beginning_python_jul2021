""" this is our blackjack game.  deal cards to users, ask them if
they want to hit or stay, etc. """

from card import Card
from deck import Deck
from player import Player

def main():
    """ this is the main function """
    print('Welcome to blackjack!')

    # set up dealer's deck
    dealer_deck = Deck([])
    for num in range(10):
        dealer_deck.add_full_deck()
    dealer_deck.shuffle()

    # get players
    players = []
    while True:
        new_name = input("Enter a player's name: ")
        if new_name:
            players.append(Player(new_name))
        else:
            break

    # deal cards to the players
    for _ in range(2):
        for player in players:
            player.add_card(dealer_deck.deal())

    for player in players:
        print(player)


if __name__ == '__main__':
    main()
