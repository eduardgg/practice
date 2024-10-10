
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = []
    minb = 1
    for i in range(len(a)):
        if a[i] == minb:
            b += [minb + 1]
            minb += 2
        else:
            b += [minb]
            minb += 1

    print(b[-1])