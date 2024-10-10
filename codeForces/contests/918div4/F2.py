
# Versió millorada, més complexa però eficient
# Utilitza un divide and conquer, i té cost O(n·logn)

def f(v):
    if len(v) == 1:
        return 0
    v1 = v[:len(v)//2]
    v2 = v[len(v)//2:]
    inter = 0

    surt1 = [(v1[i][1], i, "s1") for i in range(len(v1))]
    surt2 = [(v2[i][1], i, "s2") for i in range(len(v2))]
    entra2 = [(v2[i][0], i, "e2") for i in range(len(v2))]
    esd = surt1 + surt2 + entra2
    esd.sort()
    oberts = len(v1)
    for el in esd:
        if el[2] == "s1":
            oberts -= 1
        elif el[2] == "s2":
            inter += oberts
    return f(v1) + f(v2) + inter

t = int(input())
for _ in range(t):
    n = int(input())
    e = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        e += [(a, b)]
    e.sort()
    print(f(e))