
for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    for _ in range(5):
        a[0] += 1
        a.sort()
    print(a[0]*a[1]*a[2])