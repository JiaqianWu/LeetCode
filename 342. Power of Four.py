# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 02:12:16 2018

@author: wujiaqian
"""

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False        
        return num&(num-1)==0 and len(bin(num))%2==1

s = Solution()
r = s.isPowerOfFour(16)
print(r)