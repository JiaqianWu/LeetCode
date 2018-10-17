# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 10:12:35 2018

@author: wujiaqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isSameTree(root.left,root.right)
    def isMirror(self,p,q):
        if p == None and q == None:
            return True
        elif p and q:
            if p.val == q.val:
                return self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left)
            else:
                return False
        else:
            return False
        
            
        