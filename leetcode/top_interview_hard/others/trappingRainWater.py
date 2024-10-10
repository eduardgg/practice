class Solution(object):
    def trap(self, height):
        max_esquerra = [0]*len(height)
        max_dreta = [0]*len(height)
        for i in range(1,len(height)):
            max_esquerra[i] = max(max_esquerra[i-1],height[i-1])
            max_dreta[len(height)-1-i] = max(max_dreta[len(height)-i],height[len(height)-i])
        aigua = 0
        for i in range(1,len(height)-1):
            alt_max = min(max_esquerra[i],max_dreta[i])
            aigua += max(alt_max-height[i],0)
        return aigua       

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))
height = [4,2,0,3,2,5]
print(Solution().trap(height))