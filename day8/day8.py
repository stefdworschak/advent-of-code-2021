NUMBERS = {
    '0': 'abcefg',
    '1': 'cf',
    '2': 'acdeg',
    '3': 'acdfg',
    '4': 'bcdf',
    '5': 'abdfg',
    '6': 'abdefg',
    '7': 'acf',
    '8': 'abcdefg',
    '9': 'abcdfg',
}


def clean_data(data):
    cleaned_data = {'signal_data': [], 'output_values': []}
    for d in data:
        line = d.split(' | ')
        cleaned_data['signal_data'].append(line[0])
        cleaned_data['output_values'].append(line[1])
    return cleaned_data


def get_strings_of_unique_length(data, len_only=True):
    counter = {}
    for k, v in data.items():
        counter.setdefault(len(v), [])
        counter[len(v)].append(k)
    unique_indexes = [v[0] for v in counter.values() if len(v) == 1]
    if len_only:
        return [len(v) for k, v in data.items() if k in unique_indexes]
    return {len(v): v for k, v in data.items() if k in unique_indexes}


def challenge1(filepath):
    data = open(filepath).read().split('\n')
    cleaned_data = clean_data(data)
    unique_signals = get_strings_of_unique_length(NUMBERS)
    count = 0
    for output_value in cleaned_data['output_values']:
        filtered_ovs = [ov for ov in output_value.split(' ')
                     if len(ov) in unique_signals]
        count += len(filtered_ovs)
    return count


def get_remaining(a, b):
    return list(set(list(b)) - set(list(a)))


def decipher_signal(signal):
    letters = {}
    one = signal[0]
    four = signal[2]
    seven = signal[1]
    eight = signal[-1]
    sixes = [s for s in signal if len(s) == 6]
    fives = [s for s in signal if len(s) == 5]

    letters['a'] = ''.join(get_remaining(one, seven))
    four_plus_seven = list(set(seven + four))
    nine = [six for six in sixes if all(True if f in six else False for f in four_plus_seven )][0]
    letters['g'] = ''.join(get_remaining(''.join(four_plus_seven), ''.join(nine)))
    letters['e'] = ''.join(get_remaining(''.join(nine), ''.join(eight)))
    seven_plus_e_g = list(set(seven + letters['e'] + letters['g']))
    zero = [six for six in sixes if all(True if f in six else False for f in seven_plus_e_g)][0]
    letters['b'] = ''.join(get_remaining(''.join(seven_plus_e_g), ''.join(zero)))
    letters['d'] = ''.join(get_remaining(''.join(zero), ''.join(eight)))
    a_b_d_g = letters['a'] + letters['b'] + letters['d'] + letters['g']
    five = [f for f in fives if all(True if l in f else False for l in a_b_d_g)][0]
    letters['f'] = ''.join(get_remaining(''.join(a_b_d_g), ''.join(five)))
    letters['c'] = ''.join(get_remaining(''.join(letters['f']), ''.join(one)))

    return letters

def decrypt(data, decryption_keys):
    number = ''
    reversed_numbers = {v: k for k, v in NUMBERS.items()}
    reversed_letters = {v: k for k, v in decryption_keys.items()}
    for d in data:
        decrypted = ''.join(sorted([reversed_letters[l] for l in list(d)]))
        number += reversed_numbers[decrypted]
    return number


def challenge2(filepath):
    data = open(filepath).read().split('\n')
    numbers = []
    cleaned_data = clean_data(data)
    all_signals = cleaned_data['signal_data']
    all_ovs = cleaned_data['output_values']
    for i, signal in enumerate(all_signals):
        sorted_signals = sorted(signal.split(' '), key=len)
        decryption_keys = decipher_signal(sorted_signals)
        decrypted_output_values = decrypt(all_ovs[i].split(' '), decryption_keys)
        numbers.append(int(decrypted_output_values))
    return sum(numbers)

if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge1('day8/day8.txt')}")
    print(f"Challenge 2 Result: {challenge2('day8/day8.txt')}")
