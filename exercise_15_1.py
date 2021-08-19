cards = [(2, 'hearts'), (4, 'spades'), (6, 'diamonds')]

total = 0
for card in cards:
    print(f'{card[0]} of {card[1]}')
    total += card[0]
    answer = input('Press enter to hit, or "s" to stay ')
    if answer == 's':
        break

print(f'{total} points')
