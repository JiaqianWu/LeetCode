# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.leaflist = []
        self.helper(root)
        for i in self.leaflist:
            if i == sum:
                return True
        return False
    
    def helper(self,root):
        if root:
            if root.left:
                root.left.val += root.val
                self.helper(root.left)
            if root.right:
                root.right.val += root.val
                self.helper(root.right)
            if not root.left and not root.right:
                self.leaflist.append(root.val)