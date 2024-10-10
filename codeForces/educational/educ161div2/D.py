
line = lambda :list(map(int,input().split()))
for _ in range(int(input())):
    n = int(input())
    a = [0] + line() + [0]
    d = [0] + line() + [0]
    alive = set([i+1 for i in range(n)])
    left = [i-1 for i in range(n+2)]
    right = [i+1 for i in range(n+2)]
    for ronda in range(n):
        dies = []
        for e in alive:
            if d[e] < a[left[e]] + a[right[e]]:
                dies.append(e)
        for e in dies:
            alive.remove(e)
            left[right[e]] = left[e]
            right[left[e]] = right[e]
        print(len(dies), end=" ")
        if len(dies) == 0:
            for i in range(n - ronda - 1):
                print("0", end=" ")
            break
    print()
