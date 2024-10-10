
# Si només volem trobar els nombres primers:
N = 1000001
primes = []
isprime = [True] * N
for i in range(2, N):
    if not isprime[i]: continue
    primes.append(i)
    for j in range(i*2, N, i):
        isprime[j] = False

# Criba d'Erathostenes eficient:
# (aquí també es guarda el factor més gran de cada x,
# o bé 0 si aquell nombre és primer).
# Si s'ha de factoritzar un nombre n caldrà una criba
# de tamany, al menys, sqrt(n).
def sieve(n):
    sieve = [0]*(n+1)
    for x in range(2, n+1):
        if sieve[x]:
            continue
        for u in range(2*x, n+1, x):
            sieve[u] = x
    return sieve

s = sieve(10**6)


# Factorització eficient. Retorna un vector amb tots els
# factors de n, en ordre descendent i possibles repeticions.
def facto(n):
    f = []
    while n > 1 and s[n] != 0:
        f.append(s[n])
        n //= s[n]
    f.append(n)
    return f

# Si preferim en forma de diccionari (indicant, per cada
# clau o factor, la seva multiplicitat), usem el següent,
# amb entrada la factorització f anterior
def dicFact(f):
    d = {}
    for i in f:
        d[i] = d.get(i, 0) + 1
    return d

# NO ESTÀ TESTEJADA (usar l'anterior, de moment)
# Podem unir les dues funcions anteriors així, obtenint
# directament un diccionari a partir del nombre a factoritzar:
def dicFactInt(n):
    f = {}
    while n > 1 and s[n] != 0:
        f[s[n]] = f.get(s[n], 0) + 1
        n //= s[n]
    f[n] = f.get(n, 0) + 1
    return f

# Aquesta implementació és meva. A partir del diccionari
# anterior, generem un vector amb tots els divisors de n:
def divisors(n):

    def f(i, d):
        if i == len(v):
            divisors.append(d)
            return
        for j in range(F[v[i]]+1):
            f(i+1, d*(v[i]**j))

    F = dicFact(facto(n))
    divisors = []
    v = []
    for k in F.keys():
        v.append(k)
    f(0, 1)
    divisors.sort()
    return divisors

# S'obté un diccionari de factorització com el producte
# de dues factoritzacions, donades els seus "dicFacts".
def joinFacts(fact1, fact2):
    fact = {}
    for k in fact1.keys():
        fact[k] = fact.get(k, 0) + fact1[k]
    for k in fact2.keys():
        fact[k] = fact.get(k, 0) + fact2[k]
    return fact

# Calcula el nombre de divisors a partir de la factorització
def numDivisors(fact):
    div = 1
    for k in fact.keys():
        div *= (fact[k]+1)
    return div


# ------------------------------

n = 300
f = facto(300)
d1 = dicFact(f)
d2 = dicFactInt(n)

print(n)
print(f)
print(d1)
print(d2)

primers = sieve(1000)
print(facto(16469))
n1, n2 = 30, 6
f1, f2 = facto(n1), facto(n2)
d1, d2 = dicFact(f1), dicFact(f2)
f = joinFacts(d1, d2)
d = numDivisors(f)
print("n1 = ", n1)
print("n2 = ", n2)
print("facto(n1): f1 = ", f1)
print("facto(n2): f2 = ", f2)
print("dicFact(f1): d1 = ", d1)
print("dicFact(f2): d2 = ", d2)
print("joinFacts(d1, d2): f = ", f)
print("numDivisors(f): d = ", d)

print("divisors(24) = ", divisors(24))
print("divisors(300) = ", divisors(300))
print("sieve(50) = ", sieve(50))
print("facto(1200) = ", facto(1200))

# ------------------------------