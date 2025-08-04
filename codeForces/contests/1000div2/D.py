
for _ in range(int(input())):

    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > 2*m:
        kmax = m
    elif m > 2*n:
        kmax = n
    else:
        kmax = (n+m)//3
    print(kmax)

    a.sort()
    b.sort()
    adre = a[n//2:]
    aesq = a[:n//2]
    aesq = aesq[::-1]
    bdre = b[m//2:]
    besq = b[:m//2]
    besq = besq[::-1]

    for i in range(1, kmax+1):
        adre2, aesq2, bdre2, besq2 = adre[:], aesq[:], bdre[:], besq[:]
        n2, m2 = n, m
        ans = 0
        for e in range(i):
            if n2 == i-e:
                ans += bdre2.pop() - besq2.pop()
                n2 -= 1
                m2 -= 2
            elif m2 == i-e:
                ans += adre2.pop() - aesq2.pop()
                n2 -= 2
                m2 -= 1
            elif bdre2[-1] - besq2[-1] > adre2[-1] - aesq2[-1]:
                ans += bdre2.pop() - besq2.pop()
                n2 -= 1
                m2 -= 2
            else:
                ans += adre2.pop() - aesq2.pop()
                n2 -= 2
                m2 -= 1
        print(ans, end = " ")
    print()
