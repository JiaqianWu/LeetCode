
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 15:14:18 2018

@author: wujiaqian
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return(max(nums))

a = Solution()
b = a.maxSubArray([-2,1,-3,4,-1,2,1,7,-5,4])
print(b)
                
