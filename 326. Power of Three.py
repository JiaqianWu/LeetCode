# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:19:55 2018

@author: wujiaqian
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0