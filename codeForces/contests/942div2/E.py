
# La idea d'aquest codi tan senzill consisteix simplement
# en calcular les influències de cada valor del vector en
# el Fenwick Tree després de k iteracions. En una iteració,
# cada element en posició i afecta la posició i|i+1 en una
# k unitats, al cap de k iteracions.
# Al següent pis, o sigui j|j+1 sent j=i|i+1 tindrà una
# influència de 1+...+k = (k+1 choose 2).
# En i iteracions, serà (k+i-1 choose i) = q[i]

mod = 998244353
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, k = line()
    a = line()
    q = [1]
    for i in range(n.bit_length()):
        q.append(q[-1]*(k+i)*pow(i+1,-1,mod) % mod)
    for i in range(n):
        pis = 1
        c = a[i]
        while i|i+1 < n:
            a[i|i+1] = (a[i|i+1] - q[pis]*c) % mod
            i = i|i+1
            pis += 1
    print(*a)
