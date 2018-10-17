# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 16:55:28 2018

@author: wujiaqian
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1:
            if digits[0] == 9:
                return [1,0]
            else:
                digits[0] += 1
                return digits
        if digits[-1] + 1 > 9:
            digits[:-1] = self.plusOne(digits[:-1])
            digits[-1] = 0
            return digits
        else:
            digits[-1] += 1
            return digits


a = Solution()
b = a.plusOne([9])
print(b)


