# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 17:47:34 2018

@author: wujiaqian
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        s1 = 0
        s2 = 0
        cost.append(0)
        for i in cost:
            s1, s2 = i + min(s1,s2), s1
        return s1

test = Solution()
r = test.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1, 3, 10])
print(r)

