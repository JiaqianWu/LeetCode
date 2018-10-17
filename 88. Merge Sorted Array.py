# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:17:29 2018

@author: wujiaqian
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3
        
        Output: [1,2,2,3,5,6]
        """
        if len(nums2) == 0:
                return
        val = nums2.pop(0)
        for i in range(len(nums1)):
            if nums1[i] >= val or (nums1[i] == 0 and i >= m):
                nums1[i+1:] = nums1[i:-1]
                nums1[i] = val
                m+=1
                if len(nums2) > 0:
                    val = nums2.pop(0)
                else:
                    return
        return
    
a = Solution()
t = [-1,0,0,0,3,0,0,0,0,0,0]
a.merge(t,5,[-1,-1,0,0,1,2],6)
print(t)
