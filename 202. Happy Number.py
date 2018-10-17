# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 00:03:11 2018

@author: wujiaqian
"""

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = set()
        if n <= 0:
            return False
        while n != 1:
            a.add(n)
            sum_num = 0
            while n//10 != 0:
                sum_num += (n%10)**2
                n//=10
            sum_num += (n%10)**2
            if sum_num == 1:
                return True
            n = sum_num
            if n in a:
                return False
        return True
            