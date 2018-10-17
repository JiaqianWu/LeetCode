# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:17:41 2018

@author: wujiaqian
"""

class Solution1(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        expo = 1
        for i in range(n-1):
            expo *= i+2
        numList = list(str(expo))
        numList.reverse()
        count = 0
        for i in numList:
            if i == '0':
                count += 1
            else:
                break
        return count
    
class Solution2(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count5 = 0
        count2 = 0
        for i in range(n):
            while (i+1)%5 == 0:
                count5 += 1
                i /= 5
            while (i+1)%2 == 0:
                count2 += 1
                i /= 2
        return min(count5,count2)

class Solution3(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n//5
            n //= 5
        return count
s = Solution3()
r = s.trailingZeroes(10)
print(r)