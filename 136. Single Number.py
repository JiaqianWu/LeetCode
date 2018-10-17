# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 12:30:03 2018

@author: wujiaqian
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
        
s = Solution()
r = s.singleNumber([2,2,1])
print(r)
   