from itertools import permutations

with open("input.txt") as f:
    input = f.read().split('\n')


# Part A
def get_lights(s, e):
    lights = []
    xs = list(range(s[0], e[0] + 1))
    ys = list(range(s[1], e[1] + 1))
    lights = [(x,y) for x in xs for y in ys]
    return lights

on = {}
for ins in input:
    ins_parts = ins.split()
    end_pos = int(ins_parts[-1].split(',')[0]), int(ins_parts[-1].split(',')[1])
    start_pos = int(ins_parts[-3].split(',')[0]), int(ins_parts[-3].split(',')[1])
    action = ins_parts[0] if len(ins_parts) == 4 else ins_parts[0] + ins_parts[1]
    lights = get_lights(start_pos, end_pos)

    if action == "turnon":
       for light in lights: on[light] = True
    if action == "turnoff":
       for light in lights: on[light] = False
    if action == "toggle":
        for light in lights: on[light] = not on.get(light, False)


count = len([x for _, x in on.items() if x])
print(count)

# Part B

on = {}
for ins in input:
    ins_parts = ins.split()
    end_pos = int(ins_parts[-1].split(',')[0]), int(ins_parts[-1].split(',')[1])
    start_pos = int(ins_parts[-3].split(',')[0]), int(ins_parts[-3].split(',')[1])
    action = ins_parts[0] if len(ins_parts) == 4 else ins_parts[0] + ins_parts[1]
    lights = get_lights(start_pos, end_pos)

    if action == "turnon":
       for light in lights: on[light] = on.get(light, 0) + 1
    if action == "turnoff":
       for light in lights: on[light] = max(0, on.get(light, 1) - 1)
    if action == "toggle":
        for light in lights: on[light] = on.get(light, 0) + 2

count = sum([x for _, x in on.items()])
print(count)