# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 17:27:13 2018

@author: wujiaqian
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """        
        return str(bin(int(a,2) + int(b,2)))[2:]

    
        
