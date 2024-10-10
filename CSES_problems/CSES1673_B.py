
from collections import defaultdict

n, m = list(map(int, input().split()))
graph = defaultdict(list)
weights = defaultdict(list)
for _ in range(m):
	a, b, x = list(map(int, input().split()))
	graph[a].append(b)
	weights[a].append(-x)
	
source = 1

# Bellman Ford (adaptat):
# En l'algorisme original, si després de n iteracions, a != A,
# vol dir que hi ha algun cicle negatiu que minimitza tant com
# vulguem el camí més barat.
# Aquí faré servir una stack indicant els vèrtexos actualitzats,
# i que són per tant els únics que poden generar canvis.

inf = 10**15
A = [inf]*(n+1)
A[source] = 0
iteracions = 0

stack = [source]
while iteracions < n and stack:
	newStack = []
	a = [e for e in A]
	for v in stack:
		for i in range(len(graph[v])):
			new = a[v] + weights[v][i]
			if new < A[graph[v][i]]:
				A[graph[v][i]] = new
				newStack.append(graph[v][i])
	iteracions += 1
	stack = [e for e in newStack]

# Un cop arribats a aquí, l'stack conté els elements que es
# segueixen actualitzant, és a dir, que formen part d'un cicle
# negatiu. Mirem si des d'algun d'ells es pot arribar al destí:
vist = [False]*(n+1)
for e in stack:
	if not vist[e]:
		vist[e] = True
		dfs = [e]
		while dfs:
			v = dfs.pop()
			for w in graph[v]:
				if not vist[w]:
					vist[w] = True
					dfs.append(w)

# D'aquesta manera, tots els vèrtexs afectats pel cicle negatiu
# (i que es poden optimitzar tan com vulguem) són aquells que tenen
# vist = True. Només ens queda veure si n ho compleix.

if vist[n] or A[-1] == inf:
	print(-1)
else:
	print(-A[-1])