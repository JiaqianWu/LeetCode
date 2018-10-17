# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 13:47:32 2018

@author: wujiaqian
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in nums[1:]:
            if j != nums[i]:
                i += 1
                nums[i] = j
            else:
                continue
        return (i+1)
