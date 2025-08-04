class Solution:
    def getOperations(self, s : str) -> int:
        d = {}
        for e in s:
            d[e] = d.get(e, 0) + 1
        ans = 0
        for k in d.keys():
            ans += d[k] // 3
        return ans



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.getOperations(s)

        print(res)
        print("~")