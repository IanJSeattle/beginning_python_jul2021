""" this is our blackjack game.  deal cards to users, ask them if
they want to hit or stay, etc. """

from card import Card
from deck import Deck
from player import Player

def print_scores(dealer, players):
    """ print out everyone's score, and whether they beat the dealer or
    not. """
    for player in players:
        if player.points > 21:
            print(f'{player.name} busts with {player.points}')
            continue

        if dealer.points > 21:
            print(f'{player.name} wins with {player.points} vs. the dealer, '
                  f'who busted with {dealer.points}')
            continue

        if dealer.points > player.points:
            print(f'{player.name} loses with {player.points} vs. the dealer, '
                  f'who has {dealer.points}')
        elif player.points > dealer.points:
            print(f'{player.name} wins with {player.points} vs. the dealer, '
                  f'who has {dealer.points}')
        else:
            print(f'{player.name} ties with {player.points} vs. the dealer, '
                  f'who has {dealer.points}')

def main():
    """ this is the main function """
    print('Welcome to blackjack!')

    # set up dealer's deck
    dealer = Player('Dealer')
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
            player.add_card(dealer_deck.deal()[0])
        dealer.add_card(dealer_deck.deal()[0])

    for player in players:
        awaiting_input = True
        print(f'Hey {player.name}, your cards are:')
        while awaiting_input:
            player.show_hand()
            if player.points > 21:
                print(f'*** Bust! You have {player.points} points')
                break
            while True:
                response = input('Would you like to (h)it or (s)tay? ')
                if response == 'h':
                    player.add_card(dealer_deck.deal()[0])
                    break
                elif response == 's':
                    awaiting_input = False
                    break

    print(f'The dealer has:')
    dealer.show_hand()
    while dealer.points < 17:
        dealer.add_card(dealer_deck.deal()[0])
        print('The dealer hits, and now has:')
        dealer.show_hand()
    if dealer.points > 21:
        print(f'*** Dealer busts! with {dealer.points} points')
    elif dealer.points >= 17 and dealer.points <= 21:
        print(f'Dealer stays with {dealer.points} points')

    print_scores(dealer, players)


if __name__ == '__main__':
    main()
