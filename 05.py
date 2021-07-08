import re

with open("input.txt") as f:
    data = f.read().split('\n')

# Part B
count = 0
for word in data:
    condition_one = bool(re.search(r'(.)(.).*\1\2', word))
    condition_two = bool(re.search(r'(.).\1', word))
    count += (condition_one and condition_two)

print(count)
    
