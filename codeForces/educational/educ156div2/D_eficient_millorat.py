
# Correcte però no eficient al fer canvis de caràcters.
# Es pot arreglar modificant lleugerament l'operació, però fent inversos modulars.
# A més, a vegades caldria "dividir per 0", també s'ha d'arreglar emmagatzemant valors.

def invers_modular(a, p):
    r1, r2 = a, p
    x1, x2 = 1, 0

    while r2 > 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        x1, x2 = x2, x1 - q * x2

    if r1 != 1:
        raise ValueError(f"No existeix l'invers modular de {a} mòdul {p}")
    else:
        return x1 % p
    


modul = 998244353
n, m = list(map(int, input().split()))
s = input()
v = ['?'] + [c for c in s]

total = 1
# No inclou l'element de la posició 1 ja que si és '?', el resultat serà 0 i perdem informació.
for i in range(2, len(v)):
    if v[i] == '?':
        total *= (i-1)
        total %= modul

if v[1] == '?':
    print(0)
else:
    print(total)

for _ in range(m):
    i, c = input().split()
    i = int(i)
    if i != 1:
        if v[i] == '?' and c != '?':
            if total % (i-1) == 0:
                total //= (i-1)
            else:
                total *= invers_modular(i-1, modul)
        elif v[i] != '?' and c == '?':
            total *= (i-1)
        total %= modul

    v[i] = c
    if v[1] == '?':
        print(0)
    else:
        print(total)