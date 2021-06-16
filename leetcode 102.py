#BFS 递归# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(root, depth):
            if not root: return
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 0)
        return res

#DFS
class DFS(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def dfs(node, level, result):
            if not node:
                return
            if len(result) <= level:
                result.append([])

            result[level].append(node.val)
            dfs(node.left, level + 1, result)
            dfs(node.right, level + 1, result)

        result = []
        dfs(root, 0, result)
        return result


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        思路，BFS(node,level),level表示当前节点的层次，然后用前序递归遍历，将遍历到的节点加入到
        对应的层即可！
        '''
        levels = []
        if root == None:
            return levels
        def BFS(node,level):
            # 如果当前节点是最新的一层，则levels增加一层
            if len(levels)-1 < level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                BFS(node.left,level+1)
            if node.right:
                BFS(node.right,level+1)
        BFS(root,0)
        return levels



