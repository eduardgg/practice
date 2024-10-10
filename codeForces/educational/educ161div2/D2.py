
line = lambda :list(map(int,input().split()))
for _ in range(int(input())):
    n = int(input())
    a = [0] + line() + [0]
    d = [0] + line() + [0]
    alive = [False] + [True]*n + [False]
    cand = set([i+1 for i in range(n)])
    left = [i-1 for i in range(n+2)]
    right = [i+1 for i in range(n+2)]
    for ronda in range(n):
        dies = []
        for e in cand:
            if d[e] < a[left[e]] + a[right[e]]:
                alive[e] = False
                dies.append(e)
        cand = set()
        for e in dies:
            left[right[e]] = left[e]
            right[left[e]] = right[e]
            if alive[left[e]]:
                cand.add(left[e])
            if alive[right[e]]:
                cand.add(right[e])
        print(len(dies), end=" ")
        if len(dies) == 0:
            for i in range(n - ronda - 1):
                print("0", end=" ")
            break
    print()
