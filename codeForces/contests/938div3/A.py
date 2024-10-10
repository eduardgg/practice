
for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))
    if b >= 2*a:
        print(n*a)
    else:
        print(b*(n//2) + a*(n%2))