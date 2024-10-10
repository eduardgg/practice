def longestValidParentheses(self, s):
    D = [0]*len(s)
    for i in range(1,len(D)):
        if s[i] == "(":
            D[i] = 0
        elif s[i-1] == "(":
            D[i] = 2 + D[i-2]
        elif i-D[i-1]-1 < 0:
            D[i] = 0
        elif s[i-D[i-1]-1] == "(":
            D[i] = 2 + D[i-1] + D[i-D[i-1]-2]
        else:
            D[i] = 0

    maxim = 0
    for i in range(len(D)):
        if D[i] > maxim:
            maxim = D[i]
    return maxim
    
    # return (max(D[i] for i in range(len(s))))

s1 = "(()(()()))))()(())("
print (longestValidParentheses(s1,s1))

s2 = ")()())"
print (longestValidParentheses(s2,s2))

s3 = "()"
print (longestValidParentheses(s3,s3))