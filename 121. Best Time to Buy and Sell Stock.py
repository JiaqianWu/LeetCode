# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:15:17 2018

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
        minPrice = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit

s = Solution()
r = s.maxProfit([7,7,6,4,3,1])
print(r)