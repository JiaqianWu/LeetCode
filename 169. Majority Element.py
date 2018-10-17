# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 22:37:17 2018

@author: wujiaqian
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict.update({i:1})
        for key,value in num_dict.items():
            if value > len(nums)//2:
                return key
        return None

s = Solution()
r = s.majorityElement([3,2,2,2,20,3])
print(r)