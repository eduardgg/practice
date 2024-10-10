t = int(input())
for _ in range(t):
    q = int(input())
    fills = [[]]
    values = [0]
    for _ in range(q):
        a = list(map(int, input().split()))
        if a[0] == 1:
            values += [0]
            fills.append([])
            fills[a[1]-1].append(len(values))
            # print(fills, values, a[1])
        else:
            stack = [a[1]]
            while stack:
                e = stack.pop()
                # print(fills, values, e, a[2])
                values[e-1] += a[2]
                for fill in fills[e-1]:
                    stack.append(fill)
    for v in values:
        print(v, end=" ")
    print()