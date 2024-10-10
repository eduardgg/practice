# Sembla que funciona bé, però Time Limit

import heapq

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    a.sort()
    maxim = a[-1]
    minim = a[0]
    if minim == maxim:
        print(0)
        continue
    if k <= maxim and k >= minim:
        print(-1)
        continue
    elif k < minim:
        heap = []
        while a:
            heapq.heappush(heap, (-a.pop(), 1))
        ops = 0
        while len(heap) > 1:
            e1, q1 = heapq.heappop(heap)
            e2, q2 = heapq.heappop(heap)
            if e1 == e2:
                heapq.heappush(heap, (e1, q1+q2))
            else:
                ops += q1
                heapq.heappush(heap, (e2, q1+q2))
                heapq.heappush(heap, (-((-e1)+k-(-e2)), q1))
        print(ops)
    else:
        heap = []
        while a:
            heapq.heappush(heap, (a.pop(), 1))
        ops = 0
        while len(heap) > 1:
            e1, q1 = heapq.heappop(heap)
            e2, q2 = heapq.heappop(heap)
            if e1 == e2:
                heapq.heappush(heap, (e1, q1+q2))
            else:
                ops += q1
                heapq.heappush(heap, (e2, q1+q2))
                heapq.heappush(heap, (e1+k-e2, q1))
        print(ops)
