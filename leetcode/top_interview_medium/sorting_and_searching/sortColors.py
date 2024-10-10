class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        col0 = 0
        col1 = 0
        col2 = 0
        for i in nums:
            if i == 0:
                col0 += 1
            elif i == 1:
                col1 += 1
            else:
                col2 += 1
        return [0]*col0 + [1]*col1 + [2]*col2
        
nums = [2,0,2,1,1,0]
sol = Solution()
print(sol.sortColors(nums))