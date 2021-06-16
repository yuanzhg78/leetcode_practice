def rotateRight(self, head, k):
    if k == 0 or head is None:
        return head

    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    length = 0

    while p.next:  # 得到list的长度
        length += 1
        p = p.next

    p.next = dummy.next  # 指针指向head

    step = length - (k % length)  # 得到新head的位置

    while step > 0:  # 到新head的位置
        step -= 1
        p = p.next

    dummy.next = p.next  # 变化
    p.next = None  #

    return dummy.next




if head is None or k==0:
    return head
dummy = ListNode(0)
dummy.next = head
p=dummy
length=0
while p.next:
    length=length+1
    p=p.next
p.next=dummy.next
step=length - (k % length)
while step>0:
    step=step-1
    p=p.next
dummy.next=p.next
p.next=None
return dummy.next