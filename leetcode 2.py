# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)#re的值可以传递，所以最后返回re.next,初始化建立根结点
        r = re#定义实际操作节点
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s % 10)#确定下一个节点
            r = r.next#更新当前节点为下一个节点
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        if (carry > 0):
            r.next = ListNode(1)
        return re.next



if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(0)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(l1.next.val)
    ret = Solution().addTwoNumbers(l1, l2)
    while ret != None:
        print(ret.val)
        ret = ret.next