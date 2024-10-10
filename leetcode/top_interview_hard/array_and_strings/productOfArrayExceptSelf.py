class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        output = [0]*l
        prod = 1
        zeros = 0
        for i in range(l):
            if nums[i] == 0:
                zeros += 1
                pos = i
                continue
            prod = prod * nums[i]
        if zeros >= 2:
            return output
        if zeros == 1:
            output[pos] = prod
            return output
        for i in range(l):
            output[i] = prod // nums[i]
        return output

sol = Solution()
print(sol.productExceptSelf([-1,1,0,-3,3]))