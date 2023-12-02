def p(line):
    mx = [0]*3  
    for r in line.strip().replace('Game', '').split(':')[1].strip().split(';'):
        for i,c in [cubes.strip().split() for cubes in r.strip().split(',')]:
            mx[{'red': 0, 'green': 1, 'blue': 2}[c]] = max(mx[{'red': 0, 'green': 1, 'blue': 2}[c]], int(i))
    return mx[0]*mx[1]*mx[2]
print(sum([p(line) for line in open('day02/input.txt').readlines()]))


