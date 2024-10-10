class Solution(object):
    def getSkyline(self, buildings):
        if len(buildings) == 0:
            return []
        import heapq
        h = []
        arr = []
        lower = buildings[0][0]
        def get_height():
            return 0 if len(h) == 0 else -h[0][0]
        for x1, x2, y in buildings:
            if y == 0:
                continue
            while h and h[0][1] < x1:
                a, b = heapq.heappop(h)
                if b > lower:
                    arr.append([lower, -a])
                    lower = b
            if lower < x1 and get_height() < y:
                arr.append([lower, get_height()])
                lower = x1
            while get_height() == y:
                x2 = max(x2, heapq.heappop(h)[1])
            heapq.heappush(h, (-y, x2))
        while h:
            a, b = heapq.heappop(h)
            if b > lower:
                arr.append([lower, -a])
                lower = b
        arr.append([lower, 0])
        return arr


buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(Solution().getSkyline(buildings))