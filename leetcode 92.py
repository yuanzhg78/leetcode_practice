def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    if m == n:
        return head
    pre_dumb = ListNode(None)
    pre_dumb.next = head
    pre_last, node, count = pre_dumb, head, 1  # pre_last记录之前链表的最后一个结点
    while count < m:
        pre_last, node = node, node.next
        count += 1
    # node此时为要处理的部分的首结点，last记住这个最后会变成这部分尾结点的结点
    dumb, last = ListNode(None), node
    while count <= n:
        temp, node = node, node.next  # temp为要用头插法插入dumb的结点，node记录下一个结点
        temp.next, dumb.next = dumb.next, temp  # 将temp用头插法插入dumb
        count += 1
    # node此时为剩下部分的首节点
    pre_last.next = dumb.next
    last.next = node
    return pre_dumb.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
            h=ListNode(0)
            h.next=head
            pre=h
            cur=head
            i=1
            while i<m and cur!=None:
                pre=cur
                cur=cur.next
                i+=1
            t1=pre
            t2=cur
            while i<=n and cur!=None:
                lat=cur.next
                cur.next=pre
                pre=cur
                cur=lat
                i+=1
            t1.next=pre
            t2.next=cur
            return h.next

