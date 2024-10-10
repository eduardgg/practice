class Solution(object):

    def numSquares1(self, n):
        # Solució 1 (bàsica i mediocre, però OK)
        v = [0]
        for i in range(n):
            minim = 100
            for j in range(100):
                k = i+1-(j+1)*(j+1)
                if k >= 0 and v[k] < minim:
                    minim = v[k]
            v.append(1 + minim)
        return v[n]
        
    def numSquares2(self, n):
        # Solució 2 (recursivament, una mica millor)
        dic = {0:0}
        def f(n):
            if n in dic.keys():
                return dic[n]
            minim = 100
            for i in range(int(n**(1/2)), 0, -1):
                if n-i*i not in dic.keys():
                    dic[n-i*i] = f(n-i*i)
                if dic[n-i*i] < minim:
                    minim = dic[n-i*i]
            return 1 + minim
        return f(n)
    
    def numSquares3(self, n):
        # Solució 3 (aquest cop amb stacks)
        # Crec que és la millor de les tres
        # Per veure el procés, eliminar el "#"
        MINIM = 100
        stack = [(n,0)]
        while len(stack) > 0:
            # print(stack, "Minim: ", MINIM)
            (num, i) = stack.pop()
            if num == 0:
                MINIM = i
                continue
            if i >= MINIM-1:
                continue
            for j in range(int(num**(1/2))):
                k = num - (j+1)*(j+1)
                stack.append((k, i+1))
        return MINIM
        

sol = Solution()

print(sol.numSquares1(12))
print(sol.numSquares1(13))
print(sol.numSquares1(25))
print(sol.numSquares1(7168))
print()
print(sol.numSquares2(12))
print(sol.numSquares2(13))
print(sol.numSquares2(25))
print(sol.numSquares2(7168))
print()
print(sol.numSquares3(12))
print(sol.numSquares3(13))
print(sol.numSquares3(25))
print(sol.numSquares3(7168))