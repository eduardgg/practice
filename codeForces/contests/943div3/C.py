
for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    if n == 2:
        a = [x[0]+1, x[0]]
        print(*a)
        continue
    a = [x[0]+1]
    for i in range(n-2):
        if x[i] > x[i+1]:
            a.append(x[i])
        else:
            k = (x[i+1]-x[i])//a[i] + 1
            a.append(x[i]+k*a[-1])

    a.append(x[-1])
    print(*a)