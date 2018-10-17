# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:14:56 2018

@author: wujiaqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            if root.left and root.right:
                return min(self.minDepth(root.left),self.minDepth(root.right)) + 1 
            else:
                return self.minDepth(root.left) + self.minDepth(root.right) + 1
        