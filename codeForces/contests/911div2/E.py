import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))


def tarjan(graph):
    index = [0]  # Variable per a mantenir el comptador dels índexos DFS
    stack = []   # Pila per a mantenir els vèrtexs visitats temporalment
    result = []  # Llista per a guardar les CFC trobades
    graus = {}   # Diccionari per a guardar el grau de cada vèrtex

    def strongconnect(v):
        grau = index[0]
        index[0] += 1
        graus[v] = grau
        stack.append(v)
        onStack[grau] = True

        for w in graph[v]:
            if w not in graus:
                strongconnect(w)
                lowlink[grau] = min(lowlink[graus[v]], lowlink[graus[w]])
            elif onStack[graus[w]]:
                lowlink[grau] = min(lowlink[graus[v]], graus[w])

        if lowlink[graus[v]] == graus[v]:
            scc = []
            while True:
                w = stack.pop()
                onStack[graus[w]] = False
                scc.append(w)
                if w == v:
                    break
            result.append(scc)

    for v in range(len(graph)):
        if v not in graus:
            strongconnect(v)

    return result


def topologicalSort(graf):

    def dfs(node):
        visitats[node] = True
        for vei in graf[node]:
            if not visitats[vei]:
                dfs(vei)
        ordenament.append(node)
        return

    visitats = [False]*len(graf)
    ordenament = []
    for node in range(len(graf)):
        if not visitats[node]:
            dfs(node)

    return ordenament[::-1]


for _ in range(int(input())):
    n, m = line()
    a = line()
    g = [[] for _ in range(n)]
    for _ in range(m):
        v, u = line()
        g[v-1].append(u-1)
    # print("g graph is", g)

    lowlink = [i for i in range(n)]
    onStack = [False]*n
    sccs = tarjan(g)
    # print("sccs are", sccs)
    
    comp = [-1]*n
    for i in range(len(sccs)):
        for j in sccs[i]:
            comp[j] = i
    # print("components are", comp)
    
    h = [set() for _ in range(len(sccs))]
    for v in range(n):
        for u in g[v]:
            h[comp[v]].add(comp[u])
    for i in range(len(h)):
        h[i] = list(h[i])
    # print("h graph is", h)

    t = topologicalSort(h)
    # print("topological sort is", t)

    best = [0]*len(sccs)
    lens = [0]*len(sccs)
    for e in t:
        best[e] += sum([a[i] for i in sccs[e]])
        lens[e] += len(sccs[e])
        for f in h[e]:
            if lens[f] == lens[e]:
                best[f] = min(best[f], best[e])
            elif lens[f] < lens[e]:
                lens[f] = lens[e]
                best[f] = best[e]
    
    millor = 0
    for i in range(len(sccs)):
        if (lens[i] > lens[millor]) or (lens[i] == lens[millor] and best[i] < best[millor]):
            millor = i

    print(lens[millor], best[millor])
    