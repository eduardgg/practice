
# Find the largest rectangular area possible in a given histogram
# where the largest rectangle can be made of a number of contiguous
# bars. For simplicity, assume that all bars have the same width
# and the width is 1 unit, there will be N bars height of each bar
# will be given by the array arr.


h = [4,6,5,7,1,3,5,2,8,5,6,6,2,9,1]
n = len(h)

indEsq = []
stack = []
for i in range(n):
    while stack and h[stack[-1]] >= h[i]:
        stack.pop()
    indEsq.append(stack[-1] if stack else -1)
    stack.append(i)

indDre = []
stack = []
for i in range(n):
    while stack and h[stack[-1]] >= h[n-1-i]:
        stack.pop()
    indDre.append(stack[-1] if stack else n)
    stack.append(n-1-i)
indDre = indDre[::-1]

print(indEsq)
print(indDre)

v = [(indDre[i] - indEsq[i] - 1) * h[i] for i in range(n)]
best = max(v)
print(v)
print(best)