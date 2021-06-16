# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root : return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left , node.right = node.right , node.left
            if node.left : stack.append(node.left)
            if node.right: stack.append(node.right)
        return root




#递归
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return root
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



#https://blog.csdn.net/My_Jobs/article/details/43451187

# 根据前序遍历的顺序，优先访问根结点，然后在访问左子树和右子树。所以，对于任意结点node，第一部分即直接访问之，之后在判断左子树是否为空，
# 不为空时即重复上面的步骤，直到其为空。若为空，则需要访问右子树。注意，在访问过左孩子之后，需要反过来访问其右孩子，所以，需要栈这种数据结构的支持。对于任意一个结点node，具体步骤如下：
#
# a)访问之，并把结点node入栈，当前结点置为左孩子；
#
# b)判断结点node是否为空，若为空，则取出栈顶结点并出栈，将右孩子置为当前结点；否则重复a)步直到当前结点为空或者栈为空（可以发现栈中的结点就是为了访问右孩子才存储的）
#



#DFS前序遍历（根左右）24 ms 12.8 MB
class Solution(object):
    def invertTree(self, root):
        stack=[]
        cur=root
        while stack or cur:
            if cur != None:
                cur.left,cur.right=cur.right,cur.left
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                cur=cur.right
        return root


#中序遍历 左根右 中序遍历时要把第一层循环的cur=cur.right改成cur=cur.left。
class Solution(object):
    def invertTree(self, root):
        stack=[]
        cur=root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            cur.left,cur.right=cur.right,cur.left
            cur=cur.left
        return root
