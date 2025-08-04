
# Modificació meva del problema CSES 1087 - Shortest Subsequence
# https://cses.fi/problemset/task/1087
# Aquí considerem subseqüències contígües.

m = {'A':0, 'C':1, 'G':2, 'T':3}
mInv = {0:'A', 1:'C', 2:'G', 3:'T'}

def longestADN(s):
    n = len(s)
    l = 1
    while True:
        vist = [False]*(4**l)
        w = sum([m[s[i]]*(4**(l-1-i)) for i in range(l)])
        vist[w] = True
        for i in range(l, n):
            w -= 4**(l-1)*m[s[i-l]]
            w *= 4
            w += m[s[i]]
            vist[w] = True
        for e in range(4**l):
            if not vist[e]:
                v = []
                for _ in range(l):
                    v.append(e%4)
                    e //= 4
                seq = ''.join([mInv[c] for c in v[::-1]])
                return seq
        l += 1

s = 'ACGTACGT'
print(longestADN(s))