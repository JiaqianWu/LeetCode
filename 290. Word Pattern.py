# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:45:42 2018

@author: wujiaqian
"""

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_ls = str.split(' ')
        pat_ls = list(pattern)
        p_dict = {}
        if len(str_ls) != len(pat_ls):
            return False
        for i in range(len(pat_ls)):
            if pat_ls[i] not in p_dict.keys():
                p_dict[pat_ls[i]] = str_ls[i]
            else:
                if p_dict[pat_ls[i]] != str_ls[i]:
                    return False
        n_dict = {}
        for i in range(len(str_ls)):
            if str_ls[i] not in n_dict.keys():
                n_dict[str_ls[i]] = pat_ls[i]
            else:
                if n_dict[str_ls[i]] != pat_ls[i]:
                    return False
        return True