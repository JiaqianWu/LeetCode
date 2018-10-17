# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:54:46 2018

@author: wujiaqian
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            #recursion time complexity is 2^n
            #return self.climbStairs(n-1) + self.climbStairs(n-2)
            a1 = 1
            a2 = 2
            for i in range(n-1):
                a1,a2 = a2,a1+a2
            return a1

a = Solution()
print(a.climbStairs(3))