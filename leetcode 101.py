# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.checkTwoTree(root.left,root.right)
    def checkTwoTree(self,lefttree,righttree):
        if not lefttree and not righttree:
            return True
        if lefttree and not righttree:
            return False
        if not lefttree and righttree:
            return False
        if lefttree.val!= righttree.val:
            return False
        m=self.checkTwoTree(lefttree.left,righttree.right)
        n=self.checkTwoTree(lefttree.right,righttree.left)
        return m and n