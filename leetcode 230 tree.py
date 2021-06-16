class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ret = []
class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        stack=[]
        con=0
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            if stack:
                tmp=stack.pop()
                con += 1
                if con == k:
                    return tmp.val
                root=tmp.right



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
    root = [3,1,4,None,2]
    k=2
    treeRoot = createTree(root)
    #printTree(treeRoot)
    print(Solution().kthSmallest(treeRoot,k))