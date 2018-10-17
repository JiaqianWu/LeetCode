# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 12:15:27 2018

@author: wujiaqian
"""

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
        alist = list(alphabet)
        s = s.lower()
        newString = []
        for i in list(s):
            if i in alist:
                newString.append(i)
        if len(newString) == 0:
            return True
        for i in range(len(newString)):
            if newString[i] != newString[len(newString)-1-i]:
                return False
        return True
s = Solution()
r = s.isPalindrome("")
print(r)
                