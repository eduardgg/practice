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
        
        output = [[]]
        stack = [([], 0)]
        while len(stack) > 0:
            (v, i) = stack.pop()
            if i == len(s):
                output.append(v)
                continue
            for j in range(len(s)-i):
                if isPalindrome(s[i:i+j+1]):
                    stack.append((v + [s[i:i+j+1]], i+j+1))
        output.pop(0)
        return output


sol = Solution()
"""print(sol.partition("aab"))
print(sol.partition("aa"))
print(sol.partition("a"))"""
print(sol.partition("cdd"))