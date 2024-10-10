
from collections import defaultdict

n, m = list(map(int, input().split()))
graph = defaultdict(list)
weights = defaultdict(list)
for _ in range(m):
	a, b, x = list(map(int, input().split()))
	graph[a].append(b)
	weights[a].append(-x)
	
source = 1

# Bellman Ford ADAPTAT:
# En l'algorisme original, si després de n iteracions, a != A,
# vol dir que hi ha algun cicle negatiu que minimitza tant com
# vulguem el camí més barat.
# Aquí farem n iteracions més per assegurar que, al menys, el
# camí des de 1 fins a n no admet cap cicle d'aquests
inf = 10**15
A = [inf]*(n+1)
A[source] = 0
iteracions = 0
a = [inf]*(n+1)
while iteracions < n and a != A:
	a = [e for e in A]
	for v in graph.keys():
		for i in range(len(graph[v])):
			A[graph[v][i]] = min(A[graph[v][i]], a[v] + weights[v][i])
	iteracions += 1

# Fragment extra -> NO FUNCIONA.
ok = True
while iteracions < 2*n and a != A:
	if a[-1] != A[-1]:
		ok = False
		break
	a = [e for e in A]
	for v in graph.keys():
		for i in range(len(graph[v])):
			A[graph[v][i]] = min(A[graph[v][i]], a[v] + weights[v][i])
	iteracions += 1

print(-A[-1] if (ok and -A[-1] < inf) else -1)