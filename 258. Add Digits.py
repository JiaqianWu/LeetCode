# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 21:50:25 2018

@author: wujiaqian
"""

class Solution1(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            l = list(str(num))
            count = 0
            for i in l:
                count += int(i)
            num = count
        return num
    
class Solution2(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num-1)%9+1 if num != 0 else 0   
    