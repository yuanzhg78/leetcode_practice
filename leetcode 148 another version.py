class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        self.sort(head, None)
        return head

    def sort(self, left, right):
        if left == right or left.next == right:
            return left
        index = self.partition(left, right)
        self.sort(left, index)
        self.sort(index.next, right)

    def partition(self, left, right):
        # 前后指针法
        value = left.val
        pre = left
        cur = left
        while cur != right:
            if cur.val < value:
                pre = pre.next
                pre.val, cur.val = cur.val, pre.val
            cur = cur.next
        pre.val, left.val = left.val, pre.val
        return pre
#快速排序