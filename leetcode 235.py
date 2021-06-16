class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        maxnode = max(p.val, q.val)
        minnode = min(p.val, q.val)
        if root is None:
            return None
        if minnode <= root.val <= maxnode:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if left:
                return left
            if right:
                return right


class Solution(object):#递归
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val:  # 两个节点都在当前根节点左侧，则递归左子树
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val: # 两个节点都在当前根节点右侧，则递归右子树
            return self.lowestCommonAncestor(root.right, p, q)
        return root # 返回树根节点

