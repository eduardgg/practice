
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if k in a:
        print("YES")
    else:
        print("NO")