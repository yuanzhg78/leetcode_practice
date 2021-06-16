#全解
#https://blog.csdn.net/qq_17550379/article/details/82149899



 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:#dfs
    def pathSum(self, root: TreeNode, sunm: int) -> List[List[int]]:
        a = []
        if not root:
            return []
        def dfs(root, al):
            if root.right:
                dfs(root.right, al+[root.right.val])
            if root.left:
                dfs(root.left, al+[root.left.val])
            if not root.right and not root.left:
                if sum(al) == sunm:#求和
                    a.append(al)
        dfs(root, [root.val])
        return a


 class Solution:#递归回溯
     def pathSum(self, root, sum):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: List[List[int]]
         """
         result = list()
         if not root:
             return result

         self._pathSum(result, list(), root, sum)
         return result

     def _pathSum(self, result, path, node, num):
         if node:
             path.append(node.val)

             if not node.left and not node.right and num == node.val:
                 result.append(path.copy())

             self._pathSum(result, path, node.left, num - node.val)
             self._pathSum(result, path, node.right, num - node.val)
             path.pop()

