
# NO FUNCIONA !!! PER QUÈ ???
# Sembla que l'output no es modifica bé

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s):
            i = 0
            j = len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def f(s, v, i):
            # global output
            if i == len(s):
                output.append(v)
                print(output)
                return
            for j in range(len(s)-i):
                if isPalindrome(s[i:i+j+1]):
                    v.append(s[i:i+j+1])
                    f(s, v, i+j+1)
                    v.pop()
            return
        
        output = [[]]
        f(s, [], 0)
        output.pop(0)
        return output

sol = Solution()
print(sol.partition("aab"))