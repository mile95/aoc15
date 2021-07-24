with open("input.txt") as f:
    data = f.read()

# Part A
print(data.count('(') - data.count(')'))

# Part B
level = 0
for idx, ins in enumerate(data):
    level = level + 1 if ins == '(' else level -1
    if level == -1:
        print(idx + 1)
        break
