with open("input.txt") as f:
    data = f.read()

# Part A
x = y = 0
houses = set()
houses.add((0,0))
for move in data:
    if move == '<': x = x - 1
    if move == '>': x = x + 1
    if move == '^': y = y + 1
    if move == 'v': y = y - 1
    houses.add((x,y))

print(len(houses))

# Part B

sx = sy = rx = ry = 0
houses = set()
houses.add((0,0))
santas_turn = True
for move in data:
    if santas_turn:
        if move == '<': sx = sx - 1
        if move == '>': sx = sx + 1
        if move == '^': sy = sy + 1
        if move == 'v': sy = sy - 1
        house = (sx,sy)
    else:
        if move == '<': rx = rx - 1
        if move == '>': rx = rx + 1
        if move == '^': ry = ry + 1
        if move == 'v': ry = ry - 1
        house = (rx,ry)
    houses.add(house)
    santas_turn = not santas_turn
print(len(houses))


