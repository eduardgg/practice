# User function Template for Python3

class Solution:
    
    def maxLength(self, S):
        stack = [(0, 0)]
        ans = 0
        h = 0
        for i in range(len(S)):
            h += (1 if S[i] == '(' else -1)
            if S[i] == '(':
                stack.append((h, i+1))
            else:
                while stack and stack[-1][0] > h:
                    stack.pop()
                if stack:
                    ans = max(ans, i+1 - stack[-1][1])
                else:
                    stack.append((h, i+1))
        return ans


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends