# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 13:41:55 2018

@author: wujiaqian
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0,len(numbers)-1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
        return [i+1,j+1]

s = Solution()
r = s.twoSum([2,7,8,10,11,14,15],18)
print(r)