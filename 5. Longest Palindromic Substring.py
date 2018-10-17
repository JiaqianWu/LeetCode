# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        s_list = list(s)
        string = ''
        lenth = 0
        for i in range(len(s_list)-1):
            count = 0
            r = 0
            if s_list[i] == s_list[i+1]:
                count += 2
                for j in range(min(len(s_list)-i-2,i)):
                    if s_list[i-j-1] == s_list[i+j+2]:
                        count += 2
                        r = j+1
                    else:
                        break
                if count > lenth:
                        lenth = count
                        string = ''.join(s_list[i-r:i+r+2])
                    
            count = 1 
            for j in range(min(len(s_list)-i-1,i)):
                if s_list[i-j-1] == s_list[i+j+1]:
                    count += 2
                    r = j+1
                else:
                    break
            if count > lenth:
                    lenth = count
                    string = ''.join(s_list[i-r:i+r+1])
        return string
s = Solution()
r = s.longestPalindrome('dacbbcd')    
print(r)                