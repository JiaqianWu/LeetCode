# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 01:51:18 2018

@author: wujiaqian
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l1 = [1]
        tri = [l1]
        if numRows == 0:
            return []
        for i in range(numRows-1):
            l2 = []
            l1 = [0] + l1 + [0]
            for j in range(len(l1)-1):
                l2.append(l1[j] + l1[j+1])
            l1 = l2
            tri.append(l1)
        return tri

g = Solution()
r = g.generate(5)
print(r)