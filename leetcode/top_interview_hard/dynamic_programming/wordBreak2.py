class Solution(object):
    def wordBreak(self, s, wordDict):
        output = []
        dic = {len(s): True}

        def f(s, e, i):
            if s == "":
                # print(e)
                output.append(e[:-1])
                return
            for w in wordDict:
                if len(w) <= len(s) and s[:len(w)] == w and possible(s[len(w):], i+len(w)):
                    f(s[len(w):], e + s[:len(w)] + " ", i+len(w))
            return

        def possible(s, i):
            if i in dic.keys():
                return dic[i]
            for w in wordDict:
                if len(w) <= len(s) and s[:len(w)] == w:
                    if i+len(w) not in dic.keys():
                        dic[i+len(w)] = possible(s[len(w):], i+len(w))
                    if dic[i+len(w)]:
                        return True
            return False

        f(s, "", 0)
        return output


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

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(sol.wordBreak(s, wordDict))

s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
print(sol.wordBreak(s, wordDict))