with open('input01', 'r', encoding='utf-8') as f:
    xs = [int(x) for x in f.read().strip().splitlines()]

count = 0
for (x,y) in zip(xs, xs[1:]):
    if y > x:
        count += 1

print(f'part1: {count}') # 2 mins 56 seconds

count = 0
for i, (a,b,c) in enumerate(zip(xs[1:], xs[2:], xs[3:])):
    x, y, z = xs[i], xs[i+1], xs[i+2]
    if sum([a,b,c]) > sum([x,y,z]):
        count += 1

print(f'part2: {count}') # 8 mins 15 seconds including part 1
