with open("input.txt") as f:
    instructions = f.read().split('\n')
        
calc = dict()
results = dict()

for command in instructions:
    (ops, res) = command.split('->')
    calc[res.strip()] = ops.strip().split(' ')


def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
              res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
              res = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
              res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
              res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
              res = calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]

a = calculate('a')
print("Part A: " + str(a))

results = dict()
results['b'] = a
print("Part B: " + str(calculate('a')))

