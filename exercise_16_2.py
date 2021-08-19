my_cards = [{'value': 2, 'suit': 'hearts'},
            {'value': 7, 'suit': 'diamonds'},
            {'value': 3, 'suit': 'spades'}]

total = 0
for card in my_cards:
    value = card['value']
    suit = card['suit']
    print(f'{value} of {suit}')
    total += value

print(f'total points: {total}')
