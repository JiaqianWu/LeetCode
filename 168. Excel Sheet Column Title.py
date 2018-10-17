# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 13:48:53 2018

@author: wujiaqian
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        numList = []
        while n > 0:
            p = n%26
            n = n//26
            if p == 0:
                p = 26
                n -=1
            numList.append(p)
        for i in range(len(numList)):
            numList[i] = chr(numList[i]+64)
        numList.reverse()
        excelString = ''.join(numList)
        return excelString
s = Solution()
r = s.convertToTitle(52)
print(r)
            