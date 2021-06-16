

    def findmiddle(self,head):
        # The pointer used to disconnect the left half from the mid node.
        pre=None
        slow=head
        fast=head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        # Handling the case when slowPtr was equal to head!!!!
        if pre:
            pre.next=None
        return slow
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # If the head doesn't exist, then the linked list is empty
        if head is None:
            return None

        # Find the middle element for the list.
        middle = self.findMiddle(head)

        # The mid becomes the root of the BST.
        node = TreeNode(middle.val)

        # Base case when there is just one element in the linked list
        if head == middle:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list.
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(middle.next)
        return node


    def sortedListToBST(self, head):#最终版
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        fast, slow, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next

        pre.next = None
        next = slow.next
        slow.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(next)
        return root

