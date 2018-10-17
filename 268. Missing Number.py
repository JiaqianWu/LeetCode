# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 00:25:51 2018

@author: wujiaqian
"""

class Solution1:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return []
        max_num = max(nums)
        if len(nums) == max_num +1:
            return max_num +1
        return list(set(list(range(max_num+1)))-set(nums))[0]

class Solution2:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)