#递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(root)
        return res


#答案翻转
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left :
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]


#用模版
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
             return []
        res, stack = [], []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 比前序和中序的模板增加一个判断过程：节点没有右孩子或已经访问了该节点的子节点
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res

#https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-de-hou-xu-bian-li-die-dai-fa-by-da-da-m/
#不需要额外的判定空间


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []   # 用来存储后序遍历节点的值
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)  # 第一次入栈的是根节点
                #判断当前节点的左子树是否存在，若存在则持续左下行，若不存在就转向右子树
                node = node.left if node.left is not None else node.right
            #循环结束说明走到了叶子节点，没有左右子树了，该叶子节点即为当前栈顶元素，应该访问了
            node = stack.pop() # 取出栈顶元素进行访问
            res.append(node.val) # 将栈顶元素也即当前节点的值添加进res
            # （下面的stack[-1]是执行完上面那句取出栈顶元素后的栈顶元素）
            if stack and stack[-1].left == node: #若栈不为空且当前节点是栈顶元素的左节点
                node = stack[-1].right   ## 则转向遍历右节点
            else:
                node = None  #根据被访问节点是其父节点的的左节点或右节点就可决定下一步该怎么做：若是左节点就转到右节点；若是右节点就应该处理根节点并强制退栈。
        return res
