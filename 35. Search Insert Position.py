# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 15:05:57 2018

@author: wujiaqian
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        for i,j in enumerate(nums):
            if target <= j:
                return i
            else:
                continue
        return(len(nums))

a = Solution()
b = a.searchInsert([1,3,5,6], 6)
print(b)