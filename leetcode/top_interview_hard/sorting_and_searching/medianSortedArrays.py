class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        def f(nums1, nums2):
            if len(nums2) < 3:
                v = nums1 + nums2
                v.sort()
                if len(v) % 2 == 0:
                    return (v[len(v)//2] + v[len(v)//2 - 1]) / float(2)
                return v[len(v)//2]
            if len(nums2) % 2 != 0:
                if nums2[len(nums2)//2] > nums1[len(nums1)//2]:
                    return f(nums1[len(nums2)//2:], nums2[:len(nums2)//2+1])
                return f(nums1[:len(nums1)-len(nums2)//2], nums2[len(nums2)//2:])
            if nums2[len(nums2)//2] > nums1[len(nums1)//2]:
                return f(nums1[len(nums2)//2-1:], nums2[:len(nums2)//2+1])
            return f(nums1[:len(nums1)-len(nums2)//2+1], nums2[len(nums2)//2-1:])
        
        dif = len(nums1) - len(nums2)
        treu = (abs(dif) - 1) // 2
        if dif > 0:
            if dif > 2:
                nums1 = nums1[treu : -treu]
            return f(nums1, nums2)
        if dif < -2:
            nums2 = nums2[treu : -treu]
        return f(nums2, nums1)


nums1 = [1,4,9,14,15,16,22]
nums2 = [2,3,5,7,10,11,18,20,25,29,32,36,37]        
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))
print(sol.findMedianSortedArrays([1,2], [3,4]))