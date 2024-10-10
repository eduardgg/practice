t = int(input())
MODUL = (10**9 + 7)
for _ in range(t):
    li, ri = list(map(int, input().split()))
    suma = 0
    for i in range(2, 60):
        if li >= 2**(i+1):
            continue
        if ri < 2**i:
            break
        a = max(li, 2**i)
        b = min(ri, 2**(i+1)-1)
        # Entrem en l'interval [a, b]. En tot l'interval, f val i.
        # Hem de buscar en quins punts de l'interval canvia g.
        # De fet la g només pot valer dos valors diferents i consecutius,
        # ja que f^(g+2) i f^(g) no poden estan al mateix interval (g >= 2)
        log = 0
        num = 2**i
        while num >= i:
            num //= i
            log += 1
        suma += log*(min(i**(log+1), b+1) - a)
        suma += (log+1)*(b+1 - min(i**(log+1), b+1))
        suma %= MODUL
    print(suma)