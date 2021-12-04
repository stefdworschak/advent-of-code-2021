import re
from utils import read


def clean_data(data):
    numbers = [l.strip() for l in data.pop(0).split(',')]
    data = [d for d in data if d != '']
    cards = []
    card = ''
    for i, c in enumerate(data):
        card += ','.join([num for num in re.split('\s',c) if num != '']) + ','
        if (i+1) % 5 == 0:
           cards.append(card[:-1])
           card = ''
    checks = [','.join(len(card.split(',')) * ['0']) for j, card in enumerate(cards)]
    return numbers, cards, checks

def mark_card(number, cards, checks):
    for i, card in enumerate(cards):
        for j, c in enumerate(card.split(',')):
            if number == c:
                _checks = checks[i].split(',')
                _checks[j] = '1'
                checks[i] = ','.join(_checks)
                continue

def check_win(checks):
    # import ipdb; ipdb.set_trace()
    return any(True for c in checks if sum([int(i) for i in c]) == 5)

def chunk(checks, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(checks), n):
        yield checks[i:i + n]

def check_cards(checks):
    for i, check in enumerate(checks):
        _check = check.split(',')
        check_rows = list(chunk(_check, 5))
        check_cols = [_check[i::5] for i in range(int(len(_check)/5))]
        if check_win(check_rows) or check_win(check_cols):
            return i


def challenge(filepath, first_wins=True):
    winning_card = None
    numbers, cards, checks = clean_data(read(filepath))
    used_numbers = []
    for number in numbers:
        used_numbers.append(number)
        mark_card(number, cards, checks)
        winning = check_cards(checks)
        if winning is not None:
            # print(cards)
            winning_card = cards.pop(winning)
            winning_check = checks.pop(winning)
            # print(winning_card)
            if first_wins:
                break
            elif not cards:
                break
                
    
    unused_numbers = [int(n) for i, n in enumerate(winning_card.split(','))
                      if winning_check.split(',')[i] == '0']
    return sum(unused_numbers) * int(used_numbers[-1])


if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge('day4/day4.txt')}")
    # print(f"Challenge 2 Result: {challenge('day4/day4.txt', False)}")