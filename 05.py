import re

with open("input.txt") as f:
    data = f.read().split('\n')

# Part A
count = 0
for s in data:
    vowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
    letter_twice = [s[x] == s[x+1] for x in range(len(s) - 1)]
    forbidden_strings = [x in s for x in ['ab','cd', 'pq', 'xy']]
    if (vowels >= 3) and (True in letter_twice) and (True not in forbidden_strings):
        count += 1
print(count)

# Part B
count = 0
for word in data:
    condition_one = bool(re.search(r'(.)(.).*\1\2', word))
    condition_two = bool(re.search(r'(.).\1', word))
    count += (condition_one and condition_two)

print(count)
    
