#处理顺序和访问顺序不一致
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        cur = root #
        while stack or cur:
            while cur: # 如果cur是空的，说明左边没子节点了。
                stack.append(cur)
                cur = cur.left
            cur = stack.pop() # 左边没子节点了就输出栈顶的节点值，然后从它右边的子节点继续。
            res.append(cur.val)
            cur = cur.right
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inOrder(self, root:TreeNode, res):
        if root == None:
            return
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inOrder(root, res)
        return res
