# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:25:21 2018

@author: wujiaqian
"""

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num%2 == 0:
            num/=2
        while num%3 == 0:
            num/=3
        while num%5 == 0:
            num/=5
        if num == 1:
            return True
        else:
            return False