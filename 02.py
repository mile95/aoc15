import math

with open("input.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

# Part A
sum = 0
for entry in data:
    numbers = [int(x) for x in entry.split('x')]
    sorted_numbers = sorted(numbers)
    sum += (2*numbers[0]*numbers[1]) + (2*numbers[1]*numbers[2]) + (2*numbers[0]*numbers[2]) + (sorted_numbers[0]*sorted_numbers[1])

print(sum)

# Part B
sum = 0
for entry in data:
    numbers = [int(x) for x in entry.split('x')]
    sorted_numbers = sorted(numbers)
    sum += (2*sorted_numbers[0] + 2*sorted_numbers[1]) + math.prod(sorted_numbers)

print(sum)
    