from card import Card, CardSenseError

try:
    my_card = Card('3', 'spades')
except CardSenseError as err:
    print("whoops, that wasn't a valid card!")
    print(f'the error was: {err}')

print(f'your card is {my_card}')
