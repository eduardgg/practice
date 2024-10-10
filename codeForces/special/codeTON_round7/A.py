t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    if v[0] == 1:
        print("YES")
    else:
        print("NO")