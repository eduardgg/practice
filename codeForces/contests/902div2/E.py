
# Funciona correctament, però amb Backtracking.
# Time Limit Exceeded on test 3 (?)

n = int(input())
a = list(map(int, input().split()))

def f():
    # print(p, r, quantsP, quantsR)
    lenR = 0
    for e in r:
        if e != -1:
            lenR += 1
    if len(p) > lenR:
        return False
    if len(p) == lenR:
        if [e for e in r if e != -1] == p[:]:
            print(len(p))
            for i in p:
                print(i, end=" ")
            return True
        return False
    for i in range(len(r)):
        # print("Entered in loop with ", i)
        elem = r[i]
        if i < len(p) and p[i] == elem:
            # print("Fins aquí bé ")
            continue
        if (elem == -1) or (quantsR[elem] == quantsP[elem]):
            # print("Ja els tenim tots")
            continue
        if (quantsR[elem] < quantsP[elem]) or (quantsR[a[elem-1]] < quantsP[a[elem-1]]) or (elem == r[elem-1] and quantsR[elem] - quantsP[elem] == 1):
            # print("S'ha liat i no podem seguir per aquest camí")
            return False
        
        p.append(elem)
        quantsP[elem] += 1
        copia = None
        if r[elem-1] != -1:
            quantsR[r[elem-1]] -= 1
            copia = r[elem-1]
            r[elem-1] = -1
        
        # Recursivitat:
        if f():
            return True
        
        # Desfem els canvis
        quantsP[p.pop()] -= 1
        if copia:
            r[elem-1] = copia
            quantsR[r[elem-1]] += 1

    return False


r = a[:]
quantsR = {}
for e in r:
    quantsR[e] = quantsR.get(e, 0) + 1
p = []
quantsP = {k:0 for k in quantsR.keys()}
if not f():
    print(-1)