#BFS 递归# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
因为每层的节点值要分开记录，所以递归的参数除了节点node以外还需要当前层数level
如果节点已为空，return，结束当前递归分支即可
如果res的长度已经和当前层数level相等，说明res需要多加个位置了，因为level是res数组的索引，索引是一定比长度要小的，如果相等说明数组长度不够长了，得扩容
把当前节点加到对应层的数组中去res[level].append(node.val)
继续依次遍历左右字节点，层数level + 1
返回res
'''

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


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur =[root]
        while cur:
            tmp = []
            next_level = []
            for node in cur:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(tmp)
            cur = next_level
        return res
    

