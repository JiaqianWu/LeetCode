# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 20:53:05 2018

@author: wujiaqian
"""

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        lenth = len(matrix)
        for i in range(lenth//2):
            matrix[i], matrix[lenth-i-1] = matrix[lenth-i-1],matrix[i]
        for i in range(lenth):
            for j in range(i+1,lenth):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
                