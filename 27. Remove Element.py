# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 14:51:27 2018

@author: wujiaqian
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        flag = 0
        for i in nums:
            if i == val:
                continue
            else:
                nums[flag] = i
                flag += 1
        return (flag)

                