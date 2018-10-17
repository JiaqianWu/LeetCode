# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:34:24 2018

@author: wujiaqian
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 1
        end = x
        if x == 0: 
            return 0
        elif x == 1:
            return 1
        else:
            while end - start > 1:
                mid = int((end+start)/2)
                if mid*mid > x:
                    end = mid
                elif mid*mid < x:
                    start = mid
                else:
                    return mid
            return start
a = Solution()
print(a.mySqrt(2000))