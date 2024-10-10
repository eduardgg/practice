
# Memory limit exceeded on test 9
# Implementació una mica millor, usant diccionaris
# en comptes d'una estructura de dades per l'arbre.

line = lambda : list(map(int,input().split()))
abc = "abcdefghijklmnopqrstuvwxyz"
m = {abc[i]: i for i in range(len(abc))}

S = []
tree = {}
ans = 0
n = int(input())
for _ in range(n):
    s = input()
    S.append(s)
    ans += len(s)
    x = tree
    for i in s:
        o = ord(i) - ord('a')
        if o not in x:
            x[o] = [0, {}]
        x[o][0] += 1
        x = x[o][1]
ans *= n
for s in S:
    x = tree
    for i in s[::-1]:
        o = ord(i) - ord('a')
        if o not in x:
            break
        ans -= x[o][0]
        x = x[o][1]
ans *= 2
print(ans)