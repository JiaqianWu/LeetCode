# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 16:46:21 2018

@author: wujiaqian
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_s = s.strip()
        if len(new_s) == 0:
            return 0
        return len(new_s.split()[-1])

a = Solution()
print(a.lengthOfLastWord(' Hello '))

b = ' a '.split()[-1]