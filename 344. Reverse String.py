# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 01:56:28 2018

@author: wujiaqian
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        s_list.reverse()
        return ''.join(s_list)