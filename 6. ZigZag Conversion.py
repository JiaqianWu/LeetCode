# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:08:57 2018

@author: wujiaqian
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= 2 or numRows <= 1:
            return s
        result_list = []
        s_list = list(s)
        m = 2*(numRows-1)
        n = len(s_list)//m+1
        for i in range(numRows):
            for j in range(n):
                if m*j+i <= len(s_list)-1:
                    result_list.append(s_list[m*j+i])
                if i > 0 and i < numRows-1:
                    if m*j+m-i <= len(s_list)-1:
                        result_list.append(s_list[m*j+m-i])
        return ''.join(result_list)
    
s = Solution()
r = s.convert("PAYPALISHIRING",4)
print(r)
        
        