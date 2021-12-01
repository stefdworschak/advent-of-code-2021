from utils import read

def challenge1(filepath):
    data = read(filepath)
    last_reading = None
    count = 0
    while data:
        data_point = int(data.pop(0))
        if last_reading and data_point > last_reading:
            count += 1
        
        last_reading = data_point
    return count


def challenge2(filepath):
    data = read(filepath)
    previous_sum = None
    count = 0
    for i in range(len(data)+1):
        try:
            current_sum = sum([int(num) for num in data[(i-3):i]])
            if previous_sum and current_sum > previous_sum:
                count += 1

            previous_sum = current_sum
        except:
            continue
    return count


if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge1('day1/day1_challenge1.txt')}")
    print(f"Challenge 2 Result: {challenge2('day1/day1_challenge2.txt')}")
