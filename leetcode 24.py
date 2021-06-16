
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a, b=c.next, c.next.next
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next
        return thead.next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy=ListNode(-1)
        dummy.next=head
        s=dummy
        while s.next and  s.next.next:
            a,b=s.next,s.next.next
            s.next=b
            a.next=b.next
            b.next=a
            s=s.next.next
        return  dummy.next