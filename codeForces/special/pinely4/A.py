
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    maxim = 0
    for i in range(n):
        if not i%2 and a[i] > maxim:
            maxim = a[i]
    print(maxim)