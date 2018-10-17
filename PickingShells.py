# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 02:58:28 2018

@author: wujiaqian
"""

#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 
import math


class Solution(object):
    def shells(self, n,m):
        count = 0
        while n>m:
            n = math.ceil(9/10*(n-m))
            count += 1
        return (count+1)*m
    def select(self,n):
        low = 1
        high = n
        m = (n+1)//2
        while m-low>1 and high-m>1:
            if self.shells(n,m) < (n+1)//2:
                low = m
            else:
                high = m
            m = (low+high)//2
        if self.shells(n,low) >= (n+1)//2:
            return low
        elif self.shells(n,m) >= (n+1)//2:
            return m
        else:
            return high
if __name__ == "__main__":
    s = Solution()
    a = int(sys.stdin.readlines()[0])
    r = s.select(a)
    print(r)