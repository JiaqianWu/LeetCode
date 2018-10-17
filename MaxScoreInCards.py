# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 04:35:59 2018

@author: wujiaqian
"""

import sys 


class Solution(object):
    def count_numbers(self, n,k,s):
        list_s = list(s)
        set_s = set(list_s)
        num_list = []
        for i in set_s:
            num_list.append(s.count(i))
            num_list.sort(reverse=True)
        return num_list
    def max_score(self,n,k,s):
        result = 0
        num_list = self.count_numbers(n,k,s)
        for i in range(len(num_list)):
            if num_list[i] <= k:
                result += num_list[i]**2
                k -= num_list[i]
            else:
                result += k*num_list[i]
                break
        return result
        
if __name__ == "__main__":
    s = Solution()
    n,k = sys.stdin.readline().strip().split()
    n,k = int(n),int(k)
    s = sys.stdin.readline()[0]
    #r = s.max_score(15,10,'DZFDFZDFDDDDDDF')
    r = s.max_score(n,k,s)
    print(r)