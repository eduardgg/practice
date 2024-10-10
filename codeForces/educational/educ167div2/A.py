
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    print("YES" if a[1] >= -1 else "NO")