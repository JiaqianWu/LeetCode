# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:45:19 2018

@author: wujiaqian
"""

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n%4==0 else True