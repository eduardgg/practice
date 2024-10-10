
from collections import defaultdict
 
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	grups = defaultdict(list)
	for x in a:
		grups[str(x//4)].append(x)
	for k in grups:
		grups[k].sort(reverse = True)
	ans = []
	for e in a:
		ans.append(grups[str(e//4)].pop())
	print(*ans)