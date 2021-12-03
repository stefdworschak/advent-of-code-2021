from collections import Counter
from copy import deepcopy

from utils import read

def calculate_rates(data, decider=0):
    """ Calculates the most common number at a specific position in a binary
    number """
    gamma_rate = ''
    epsilon_rate = ''
    bin_length = len(data[0])
    binaries = list(''.join(data))
    for l in range(bin_length):
        nth_binary = binaries[l::bin_length]
        counted = Counter(nth_binary)
        # print(counted)
        if counted['0'] > counted['1']:
            gamma_rate += '0'
            epsilon_rate += '1'
        elif counted['0'] == counted['1']:
            gamma_rate += str(decider)
            epsilon_rate += str(int(not decider))
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    return gamma_rate, epsilon_rate


def search_rating(searchstring, data, search_index):
    """ Search (from the back) for all strings starting with a subset of 
    of a searchstring """
    searchstring = calculate_rates(data, decider=1)[search_index]
    search = ''
    matches = data
    i = 0
    while len(matches) > 1 or i > 12:
        search += searchstring[i]
        matches = [d for d in matches if d.startswith(search)]
        searchstring = calculate_rates(matches, decider=1)[search_index]        
        i += 1
    return matches[0]

def to_decimal(num):
    """ Converts a number to decimal """
    return int(num, 2)


def challenge1(filepath):
    data = deepcopy(read(filepath))
    gamma_rate, epsilon_rate = calculate_rates(data)
    print(to_decimal(gamma_rate))
    print(to_decimal(epsilon_rate))
    return to_decimal(gamma_rate) * to_decimal(epsilon_rate)

def challenge2(filepath):
    data = deepcopy(read(filepath))
    gamma_rate, epsilon_rate = calculate_rates(data, decider=1)
    oxygen_generator_rating = search_rating(gamma_rate, data, 0)
    co2_scrubber_rating = search_rating(epsilon_rate, data, 1)
    print(to_decimal(oxygen_generator_rating))
    print(to_decimal(co2_scrubber_rating))
    return to_decimal(oxygen_generator_rating) * to_decimal(co2_scrubber_rating)


if __name__== '__main__':
    # print(f"Result Challenge 1: {challenge1('day3/day3_test.txt')}")
    print(f"Result Challenge 1: {challenge2('day3/day3.txt')}")
