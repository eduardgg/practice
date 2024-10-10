import math

# Aquesta és una implementació meva, no tan bona.
# Trobar la bona (eficient) a factorizeBo.py

# Càlcul de la criba d'Eratòstenes
def erathostenes(n):
    v = [0, 0] + [1]*(n-1)
    for i in range(2, n+1):
        if v[i] == 0:
            continue
        if v[i] == 1:
            j = 2*i
            while j <= n:
                v[j] = 0
                j += i
    return [p for p in range(n+1) if v[p] == 1] 

# Factorització d'n en forma de diccionari:
# (indica el nombre de factors de cada clau)
def factorize(n):
    F = {}
    primers = erathostenes(int(math.sqrt(n)))
    for p in primers:
        if n in primers:
            F[n] = F.get(n, 0) + 1
            break
        if p*p > n:
            break
        while n % p == 0:
            F[p] = F.get(p, 0) + 1
            n //= p
    if n != 1:
        F[n] = 1
    return F

# Retorna un vector dels divisors ordenats
# (i amb possibles repeticions) d'n:
def divisors(n):

    def f(i, d):
        if i == len(v):
            divisors.append(d)
            return
        for j in range(F[v[i]]+1):
            f(i+1, d*(v[i]**j))

    F = factorize(n)
    divisors = []
    v = []
    for k in F.keys():
        v.append(k)
    f(0, 1)
    divisors.sort()
    return divisors

# Crea un diccionari de la factorització de n1*n2.
# a partir de les factoritzacions separades de n1 i n2.
def joinFacts(fact1, fact2):
    fact = {}
    for k in fact1.keys():
        fact[k] = fact.get(k, 0) + fact1[k]
    for k in fact2.keys():
        fact[k] = fact.get(k, 0) + fact2[k]
    return fact

# Calcula el nombre de divisors d'n, donada la factorització.
def numDivisors(fact):
    div = 1
    for k in fact.keys():
        div *= (fact[k]+1)
    return div


# ------------------------------

primers = erathostenes(1000)
print(primers)
print(factorize(16469))
f1 = factorize(30)
f2 = factorize(6)
f = joinFacts(f1, f2)
d = numDivisors(f)
print(f1)
print(f2)
print(f)
print(d)
print(divisors(24))
print(divisors(300))

# ------------------------------