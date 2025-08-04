
n = int(input())
ans = [0]
for i in range(n):
    ans += [(1<<i) + ans[-1-j] for j in range(2**i)]
for e in ans:
    for i in range(n-1,-1,-1):
        print(1 if e & (1<<i) else 0, end = "")
    print()