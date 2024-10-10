
for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    last = p.pop()
    q = [last] + p
    print(*q)