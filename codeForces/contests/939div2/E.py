
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    while True:
        zero = None
        for i in range(1, n+1):
            a[i%n] -= a[i-1]
            if a[i%n] <= 0:
                a[i%n] = 0
                zero = i
        if zero == None:
            continue
        cont = 0
        ok = True
        for i in range(n):
            if a[(zero+i)%n] != 0:
                cont += 1
                if cont >= 4:
                    ok = False
                    break
            else:
                cont = 0
        if ok:
            break
    
    if a[0] > 0:
        a[1] = max(0, a[1]-a[0])
        if a[1] > 0 and len(a) > 2:
            a[2] = max(0, a[2]-a[1])

    i = 0
    while i < n:
        if a[(zero+i)%n] == 0:
            i += 1
        else:
            if a[(zero+1+i)%n] == 0:
                i += 2
            elif a[(zero+2+i)%n] == 0:
                a[(zero+1+i)%n] = 0
                i += 3
            else:
                y = a[(zero+1+i)%n]
                x = a[(zero+i)%n]
                k = y//x
                a[(zero+1+i)%n] = 0
                a[(zero+2+i)%n] += k*(k+1)*x//2 - k*y
                i += 4
    

    ans = [i+1 for i in range(n) if a[i] > 0]
    print(len(ans))
    print(*ans)