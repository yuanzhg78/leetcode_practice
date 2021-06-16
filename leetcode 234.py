#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head==None or head.next==None:
            return True
        fast=head.next
        slow=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next#找到链表的中点
        pre=slow.next
        #slow.next=None
        p=None
        while pre is not None:#反转后半部分
                q=pre.next
                pre.next=p
                p=pre
                pre=q
        while p is not None and head is not None:
                    if p.val != head.val:
                        return False
                    p,head=p.next,head.next
        return True


def createList():
    head = ListNode(0)
    cur = head
    for i in range(1, 4):
        cur.next = ListNode(i)
        cur = cur.next
    return head


def printList(head):
    cur = head
    while cur != None:
        print(cur.val, '-->', end='')
        cur = cur.next

    print('NULL')


if __name__ == "__main__":
    head = createList()
    printList(head)
    res = Solution().isPalindrome(head)
    print(res)
# 设置快慢指针
# 每次快指针增加两个，慢指针增加一个
# 这样当快指针结尾时，慢指针指向了链表的中间
# 用慢指针逆序链表的后半部分，利用Python交换的特性，不需要额外的tmp结点
# 一个从头开始，一个从中间开始，判断两者是否相同
