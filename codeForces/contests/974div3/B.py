
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if n%2: print("YES" if k%4 in {0, 3} else "NO")
    else: print("YES" if k%4 in {0, 1} else "NO")