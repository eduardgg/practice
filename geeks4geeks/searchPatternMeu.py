class Solution:
    def search(self, pat, txt):
        mod = 10**9+7
        p = pow(26, len(pat)-1, mod)
        ans = []
        hashPat = 0
        for c in pat:
            hashPat *= 26
            hashPat += ord(c)-96
            hashPat %= mod
        hashTxt = 0
        for i in range(len(txt)):
            if i >= len(pat):
                hashTxt -= (ord(txt[i-len(pat)])-96)*p
            hashTxt *= 26
            hashTxt += ord(txt[i])-96
            hashTxt %= mod
            if hashTxt == hashPat:
                ans.append(i-len(pat)+1)
        return ans

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()