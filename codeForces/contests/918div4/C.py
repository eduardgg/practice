import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    sr = int(math.sqrt(s))
    if sr ** 2 == s:
        print("YES")
    else:
        print("NO")