class Solution(object):
    def wordBreak0(self, s, wordDict):
        dic = {}
        def f(s):
            if s == "":
                return True
            for w in wordDict:
                if len(w) <= len(s) and s[:len(w)] == w:
                    if s[len(w):] not in dic.keys():
                        dic[s[len(w):]] = f(s[len(w):])
                        # print(dic)
                    if dic[s[len(w):]]:
                        return True
            return False
        return f(s)

    def wordBreak(self, s, wordDict):
        # Petita millora respecte de l'anterior
        # (El diccionari conté posicions, no strings)
        dic = {}
        def f(s,i):
            if s == "":
                return True
            for w in wordDict:
                if len(w) <= len(s) and s[:len(w)] == w:
                    if i+len(w) not in dic.keys():
                        dic[i+len(w)] = f(s[len(w):],i+len(w))
                        # print(dic)
                    if dic[i+len(w)]:
                        return True
            return False
        return f(s,0)

sol = Solution()

s = "applepenapple"
wordDict = ["apple","pen"]
print(sol.wordBreak(s, wordDict))

s = "leetcode"
wordDict = ["leet","code"]
print(sol.wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(sol.wordBreak(s, wordDict))

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(sol.wordBreak(s, wordDict))