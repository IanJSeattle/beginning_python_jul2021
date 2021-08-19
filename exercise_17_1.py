my_cards = [{'value': 2, 'suit': 'hearts'},
            {'value': 7, 'suit': 'diamonds'},
            {'value': 3, 'suit': 'spades'}]

def count_with_loop(cards):
    total = 0
    for card in cards:
        value = card['value']
        total += value
    return total


def count_with_sum(cards):
    return sum([item['value'] for item in cards])


print(f'total with loop is {count_with_loop(my_cards)}')
print(f'total with sum is {count_with_sum(my_cards)}')
