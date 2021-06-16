class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ret = []
class Solution:
    def constructFromPrePost(self, pre, post) -> TreeNode:
        if len(pre) == 0 or len(post) == 0:
            return None

        root = TreeNode(pre[0])
        stack = [root]
        curr = root
        post_pointer = 0
        for i in range(1, len(pre)):
            if not curr.left:
                curr.left = TreeNode(pre[i])
                stack.append(curr.left)
            else:
                curr.right = TreeNode(pre[i])
                stack.append(curr.right)
            curr = stack[-1]
            while curr.val == post[post_pointer]:
                stack.pop()
                if not stack:
                    break
                curr = stack[-1]
                post_pointer += 1
        return root


def createTree(root):
    if root == None:
        return root

    Root = TreeNode(root[0])
    nodeQueue = [Root]
    index = 1
    front = 0
    while index < len(root):
        node = nodeQueue[front]

        item = root[index]
        index += 1
        if item != None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(root):
            break

        item = root[index]
        index += 1
        if item != None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

        front += 1

    return Root


def printTree(root):
    if root != None:
        print(root.val)
        printTree(root.left)
        printTree(root.right)


if __name__ == "__main__":
    #root = [3,9,20,None,None,15,7]
    pre=[1,2,4,5,3,6,7]
    post=[4,5,2,6,7,3,1]

    #pre = createTree(pre)
    #post=createTree(post)
    res=Solution().constructFromPrePost(pre,post)