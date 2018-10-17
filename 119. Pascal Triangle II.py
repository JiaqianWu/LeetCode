# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 01:55:51 2018

@author: wujiaqian
"""

class Solution:
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l1 = [1]
        if rowIndex == 0:
            return l1
        for i in range(rowIndex):
            l2 = []
            l1 = [0] + l1 + [0]
            for j in range(len(l1)-1):
                l2.append(l1[j] + l1[j+1])
            l1 = l2
        return l1

g = Solution()
r = g.generate(5)
print(r)