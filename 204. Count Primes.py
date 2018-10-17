# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 22:10:04 2018

@author: wujiaqian
"""

class Solution1(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(n):
            if self.isPrime(i):
                count += 1
        return count
    def isPrime(self,num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
class Solution2(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        l = [1]*n
        l[0]=l[1]=0
        l[2]=1
        for i in range(2,n):
            if l[i] == 1:
                for j in range(2,(n-1)//i+1):
                    l[i*j]=0
        return sum(l)
            
        
        
        
s = Solution2()
r = s.countPrimes(999983)
print(r)