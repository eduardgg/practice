#User function Template for python3
class Solution:
    def findLongestWord (ob, S, d):
        pos = {w:0 for w in d}
        for c in S:
            for w in d:
                if pos[w] < len(w) and w[pos[w]] == c:
                    pos[w] += 1
        best = ""
        print(pos)
        for w in d:
            if pos[w] == len(w) > len(best) and w < best:
                best = w
        return best
    
d = {"ale", "apple", "monkey", "plea"}
s = "abpcplea"
print(Solution().findLongestWord(s, d))

