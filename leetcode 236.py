def lowestCommonAncesto1r(self, root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None: return None
        if root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)#处理所有左边的树，后面两个参数随时进行搜素， 返回p和q其中一个值
        right = self.lowestCommonAncestor(root.right, p, q)#处理所有右边的树
        #left和right至少有一边是null
        if left == None:
            return right
        if right == None:
            return left
        #left 和 right 都返回not null
        return root
    #time O(N) 树上节点的数量
    #空间 递归
    #logN worstO(N)



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
    root=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    k=2
    treeRoot = createTree(root)
    #printTree(treeRoot)
    print(Solution().lowestCommonAncestor(treeRoot,5,1))