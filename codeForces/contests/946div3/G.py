
from heapq import heappop, heappush

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    m, x = line()
    c = line()
    money = 0
    heap = []
    for cost in c:
        if money >= cost:
            heappush(heap, -cost)
            money -= cost
        else:
            if heap:
                worst = -heappop(heap)
                if cost < worst:
                    heappush(heap, -cost)
                    money += worst - cost
                else:
                    heappush(heap, -worst)
        money += x
    print(len(heap))