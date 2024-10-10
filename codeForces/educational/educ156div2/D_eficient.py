
# Correcte però no eficient al fer canvis de caràcters.
# Es pot arreglar modificant lleugerament l'operació, però fent inversos modulars.
# A més, a vegades caldria "dividir per 0", també s'ha d'arreglar emmagatzemant valors.

def fer():

    if s[1] == '?':
        print(0)
        return
    
    total = 1
    for i in range(2, len(s)):
        if s[i] == '?':
            total *= (i-1)
            total %= modul

    print(total)
    return


modul = 998244353
n, m = list(map(int, input().split()))
s = '?' + input()
# print(s)
fer()

for _ in range(m):
    i, c = input().split()
    i = int(i)
    s = s[:i] + c + s[i+1:]
    # print(s)
    fer()