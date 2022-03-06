# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #stack 栈记录
        # 检测结点为空的情况
        if not root:
            return []
        stack = [root]
        res = []
        # 当栈为空的时候，说明已经遍历完成
        while stack:
            cur = stack.pop()#弹出当前root节点
            #先处理中间节点
            res.append(cur.val)
            # 再处理右孩子，因为右边先入栈，左边再入栈，出栈的时候才是先左再右
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

class Solution:
    def preorderTraversal(self, root: TreeNode):
        #用于存放结果
        result = []
        #把root节点存入栈中
        stack = [root]
        #检测结点为空的情况
        if root == None:
            return []
        #当栈为空的时候，说明已经遍历完成
        while stack:
            node = stack.pop() #弹出root节点
            #先处理中间节点
            result.append(node.val)
            #再处理右孩子，因为右边先入栈，左边再入栈，出栈的时候才是先左再右
            if node.right:
                stack.append(node.right)
            #最后处理左节点
            if node.left:
                stack.append(node.left)
        return result
