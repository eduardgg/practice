
for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    suma = sum(a)
    if suma %2 != 0:
        print(-1)
    elif a[2] >= a[1]+a[0]:
        print(a[1]+a[0])
    else:
        print(sum(a)//2)