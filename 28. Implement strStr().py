# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 14:59:09 2018

@author: wujiaqian
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)+1-len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
            else:
                continue
        return -1
