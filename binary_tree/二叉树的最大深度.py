#用层序遍历的方法
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 方法1：BFS广度优先遍历
        queue = [root]
        res = 0
        if not root:
            return 0
        while queue:    # 要遍历的新层节点非None
            res += 1
            nlist = []
            for node in queue:    # 要遍历的新层节点
                if node:
                    if node.left:
                        nlist.append(node.left)    # 存储非None空的下层节点
                    if node.right:
                        nlist.append(node.right)
            queue = nlist    # 迭代下层节点
        return res
#递归
class solution:
    def maxdepth(self, root: treenode) -> int:
        return self.getdepth(root)

    def getdepth(self, node):
        if not node:
            return 0
        leftdepth = self.getdepth(node.left)  # 左
        rightdepth = self.getdepth(node.right)  # 右
        depth = 1 + max(leftdepth, rightdepth)  # 中
        return depth

#很好的帖子
#https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/python-3di-gui-zi-ding-xiang-xia-zi-di-xiang-shang/
#自顶而下
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def top_down(node, h):
            return h if node is None else max(top_down(node.left, h + 1), top_down(node.right, h + 1))
        return top_down(root, 0)
#自底而上
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def bottom_up(node):
            return 0 if node is None else max(bottom_up(node.left), bottom_up(node.right)) + 1
        return bottom_up(root)

#https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/er-cha-shu-de-zui-da-shen-du-by-jezkahsq-pqz6/