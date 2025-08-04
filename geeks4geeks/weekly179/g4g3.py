from typing import List


class Solution:
    def isPossible(self, n : int, arr : List[int]) -> int:
        dosos = [0]
        cincs = [0]
        for e in arr:
            dosos.append(dosos[-1])
            cincs.append(cincs[-1])
            while not e%2:
                dosos[-1] += 1
                e //= 2
            while not e%5:
                cincs[-1] += 1
                e //= 5
        for i in range(1, n+1):
            if min(dosos[i], cincs[i]) == min(dosos[-1] - dosos[i], cincs[-1] - cincs[i]):
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


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.isPossible(n, arr)

        print(res)
        print("~")