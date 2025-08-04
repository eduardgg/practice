from typing import List


class Solution:
    def minXOR(self, n : int, k : int, arr : List[int]) -> int:
        xor = 0
        for e in arr:
            xor ^= e
        while xor and k:
            xor &= (1 << (xor.bit_length() - 1)) - 1
            k -= 1
        return xor




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

        k = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.minXOR(n, k, arr)

        print(res)
        print("~")