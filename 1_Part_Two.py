numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
           'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}

def find_all(string, substring):
    """
    Credits: https://stackoverflow.com/a/4665027/12485764
    """
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1: return
        yield start
        start += 1

with open('1_input.txt', 'r') as f:
    lines = f.read().splitlines()

sums = []

for line in lines:
    nums_in_line = {}
    for i in range(len(line)):
        if line[i].isnumeric():
            nums_in_line[i] = int(line[i]) # index : value in dict
    for word_number in numbers.keys():
        if find_all(line, word_number) != -1:
            for number in list(find_all(line, word_number)):
                nums_in_line[number] = numbers[word_number]
    sums.append(int(str(nums_in_line[min(nums_in_line.keys())]) + str(nums_in_line[max(nums_in_line.keys())])))

print(sum(sums))