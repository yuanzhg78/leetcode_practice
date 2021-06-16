class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        #get the lengh of list 获取链表长度
        length = 1
        cur = head.next
        while cur:
            length += 1
            cur = cur.next
        #哑结点
        dummy = ListNode(0)
        dummy.next = head

        n = 1
        while n<length:
            cur = dummy.next
            tail = dummy
            while cur:
                left = cur
                right = self.split(left, n)#返回右边的head
                cur = self.split(right,n)#下一组的head即rest的head
                merged = self.merge(left,right)
                tail.next = merged[0]
                tail = merged[1]
            n <<= 1 #乘2
        return dummy.next

    # Splits the list into two parts, first n element and the rest.
    # Returns the head of the rest.
    def split(self,head,n):
        while n > 1 and head:
            head = head.next
            n-= 1
        if head:
            rest = head.next
            head.next = None  #cut掉和rest的连接 将下一个变为none
        else:
            rest = None
        return rest #返回的是rest的head

    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        while tail.next:
            tail = tail.next #注意将tail放到最后一个，返回归并完的结果的tail位置
        return [dummy.next, tail]
