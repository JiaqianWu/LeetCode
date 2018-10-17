# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:33:57 2018

@author: wujiaqian
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        maxProfit = 0
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i] > 0:
                maxProfit += prices[i+1]-prices[i]
        return maxProfit

s = Solution()
r = s.maxProfit([7,1,5,3,6,4])
print(r)