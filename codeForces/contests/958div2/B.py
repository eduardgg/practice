
for _ in range(int(input())):
    n = int(input())
    a = input()
    uns, zeros = 0, 0
    last = 1
    for e in a:
        if e == '1':
            uns += 1
        elif last != 0:
            zeros += 1
        last = int(e)
    print("YES" if uns > zeros else "NO")