# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:16:23 2018

@author: wujiaqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            if abs(r-l) >= 2:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
    def maxDepth(self,root):
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        

