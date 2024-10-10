
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if any([(a[i]-a[0])%2 for i in range(n)]):
        print(-1)
        continue
    maxim = max(a)
    ops = []
    while maxim > 1:
        ops.append(maxim//2)
        maxim -= maxim//2
    if maxim == 1:
        ops.append(1)
    print(len(ops))
    print(*ops)