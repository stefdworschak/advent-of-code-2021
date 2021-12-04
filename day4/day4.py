import re
from utils import read


def clean_data(data):
    numbers = [l.strip() for l in data.pop(0).split(',')]
    cards = []
    card = ''
    for i, c in enumerate(data):
        if c: 
            card += ','.join([num for num in re.split('\s',c) if num != '']) + ','
        # if c:
        #     card.append([num for num in re.split('\s',c) if num != ''])
        #     print([num for num in re.split('\s',c) if num != ''])
        if i % 5 == 0 and i > 0:
           cards.append(card[:-1])
           card = ''
    checks = [','.join(len(card.split(',')) * ['0']) for i, card in enumerate(cards)]
    return numbers, cards, checks

def mark_card(number, cards, checks):
    index = None
    for i, card in enumerate(cards):
        for j, c in enumerate(card.split(',')):
            if number == c:
                _checks = checks[i].split(',')
                _checks[j] = '1'
                checks[i] = ','.join(_checks)
                continue


def chunk(checks, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(checks), n):
        yield checks[i:i + n]

def check_cards(checks):
    for check in checks:
        _check = check.split(',')
        import ipdb; ipdb.set_trace()
        _check = list(chunk(_check, 5))



def challenge1(filepath):
    numbers, cards, checks = clean_data(read(filepath))
    for number in numbers:
        # print(number)
        mark_card(number, cards, checks)
        # print(checks)
        check_cards(checks)
    print(checks)
    # for number in numbers:

    print(cards)



if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge1('day4/day4_test.txt')}")
    # print(f"Challenge 2 Result: {challenge2('day1/day1_challenge2.txt')}")
