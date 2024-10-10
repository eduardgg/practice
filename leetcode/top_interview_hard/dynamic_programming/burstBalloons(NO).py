class Solution(object):
    def maxCoins(self, nums):

        # Funciona, però NO EFICIENT!

        dic = {}
        def f(vector):
            if len(vector) == 1:
                return vector[0]
            maxim = 0
            for i in range(len(vector)):
                vec = vector[:i] + vector[i+1:]
                if tuple(vec) not in dic.keys():
                    dic[tuple(vec)] = f(vec)
                valor = vector[i]
                if i < len(vector)-1:
                    valor = valor * vector[i+1]
                if i > 0:
                    valor = valor * vector[i-1]
                valor = valor + dic[tuple(vec)]
                if valor > maxim:
                    maxim = valor
            return maxim 
        return f(nums)


nums = [3,1,5,8]
nums = [1,5]
nums = [1,6,8,3,4,6,4,7,9,8,0,6,2,8]
sol = Solution()
print(sol.maxCoins(nums))