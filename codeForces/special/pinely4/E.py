
from collections import defaultdict

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    g = defaultdict(list)
    for _ in range(m):
        u, v = list(map(int, input().split()))
        g[u].append(v)
        g[v].append(u)
    color = [-1]*(n+1)
    color[1] = 1
    stack = [1]
    odd = False
    while stack:
        v = stack.pop()
        for i in g[v]:
            if color[i] == color[v]:
                odd = True
                stack = []
                break
            if color[i] == -1:
                color[i] = 1-color[v]
                stack.append(i)
    
    if odd:
        print("Alice")
        for i in range(n):
            print("1 2", flush = True)
            ans = input()
    else:
        part1, part2 = [], []
        for i in range(1, n+1):
            if color[i] == 0:
                part1.append(i)
            else:
                part2.append(i)

        print("Bob")
        left1, left2 = len(part1), len(part2)
        for i in range(n):
            c1, c2 = list(map(int, input().split()))
            if 1 in {c1, c2} and left1:
                print(part1.pop(), 1, flush = True)
                left1 -= 1
            elif 2 in {c1, c2} and left2:
                print(part2.pop(), 2, flush = True)
                left2 -= 1
            elif left1:
                print(part1.pop(), 3, flush = True)
                left1 -= 1
            else:
                print(part2.pop(), 3, flush = True)
                left2 -= 1