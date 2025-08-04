
from typing import List


class Solution:

    def isEqual(self, n : int, q : int, A : List[int], queries : List[List[int]]) -> int:
        
        if sum(A)%2:
            return 0

        rank = [1]*(n)
        leader = list(range(n))

        def find(u):
            if leader[u] == u:
                return u
            leader[u] = find(leader[u])
            return leader[u]

        def union(a, b):
            la = leader[a]
            lb = leader[b]
            if rank[la] > rank[lb]:
                imp[la] += imp[leader[lb]]
                leader[lb] = la
            elif rank[la] < rank[lb]:
                imp[lb] += imp[leader[la]]
                leader[la] = lb
            else:
                imp[la] += imp[leader[lb]]
                leader[lb] = la
                rank[la] += 1
            return

        imp = A[:]
        for a, b in queries:
            union(a-1, b-1)
        
        lids = set()
        for i in range(n):
            if i == leader[i]:
                lids.add(i)

        total = sum([imp[i] for i in lids])
        vals = set()
        vals.add(0)
        for e in lids:
            new = {i for i in vals}
            for i in new:
                va = imp[e] + i
                if va <= total // 2 and va not in vals:
                    vals.add(va)
                    if va == total // 2:
                        return 1
        
        return 0



        



class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        q = int(input())

        A = IntArray().Input(n)

        queries = IntMatrix().Input(q, 2)

        obj = Solution()
        res = obj.isEqual(n, q, A, queries)

        print(res)
        print("~")
