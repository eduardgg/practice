
# Memory limit exceeded on test 6
# Implementació inventada per mi, fent servir una
# estructura de dades d'un arbre. Falta memòria.

class Node:
    def __init__(self):
        self.v = [0]*26
        self.f = [None]*26

line = lambda : list(map(int,input().split()))
abc = "abcdefghijklmnopqrstuvwxyz"
m = {}
for i in range(len(abc)):
    m[abc[i]] = i

S = []
u = 0
n = int(input())
root = Node()
for _ in range(n):
    s = input()
    S.append(s)
    u += len(s)
    node = root
    for i in s:
        node.v[m[i]] += 1
        if not node.f[m[i]]: 
            node.f[m[i]] = Node()
        node = node.f[m[i]]
    
C = 0
for s in S:
    node = root
    for i in s[::-1]:
        C += node.v[m[i]]
        node = node.f[m[i]]
        if not node:
            break

print(2*n*u - 2*C)