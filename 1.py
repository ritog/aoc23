with open('1_input.txt', 'r') as f:
    data = f.read().splitlines()

sums = []

for string in data:
    numbers_in_line = []
    for letter in string:
        if letter.isnumeric():
            numbers_in_line.append(int(letter))
    sums.append(int(str(numbers_in_line[0]) + str(numbers_in_line[-1])))

print(sum(sums))  