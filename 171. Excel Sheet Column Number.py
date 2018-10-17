# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:11:33 2018

@author: wujiaqian
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sList = list(s)
        result = 0
        for i in range(len(sList)):
            n = len(sList)-i-1
            result += (ord(sList[i])-64)*(26**n)
        return result

s = Solution()
r = s.titleToNumber('ZZ')
print(r)