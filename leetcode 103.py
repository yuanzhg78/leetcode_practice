class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:return None
        root = TreeNode(preorder[0])
        dicts= {val:i for i,val in enumerate(inorder)}#构建值和其在中序遍历的位置序号对应的字典
        stack= [root]
        for i in range(1,len(preorder)):
            num = preorder[i]
            idx = dicts[num]
            interval = TreeNode(num)
            #如果这个数的位置序号比栈中最后一个小，说明你是栈中最后一个的左子树，
            if idx < dicts[stack[-1].val]:
                stack[-1].left=interval
                stack.append(interval)
            #比最后一个大，说明此时是某个节点的右子树
            else:
                #出栈，使temp的val的index比idx小，idx作为temp的右子树
                while stack and idx > dicts[stack[-1].val]:#终止条件为栈为空，或者idx<栈顶元素序号，说明idx应该在栈顶元素的左子树中。
                    temp = stack.pop()
                temp.right = interval
                stack.append(interval)
        return root



#递归
class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if not inorder: return
        root = TreeNode(preorder.pop(0))#因为前序遍历的第一个节点是root
        i = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:i])
        root.right = self.buildTree(preorder, inorder[i+1:])
        return root



