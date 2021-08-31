# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
#
# 在链表类中实现这些功能：
#
# get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 定义头节点,尾节点,链表长度
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if not self.dummy.next or index > self.length - 1:
            return -1
        p = self.dummy.next
        while index:
            p = p.next
            index -= 1
        return p.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newnode = ListNode(val)
        if not self.dummy.next:
            self.dummy.next = newnode
            self.tail = newnode
        else:
            q = self.dummy.next
            self.dummy.next = newnode
            newnode.next = q
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newnode = ListNode(val)
        self.tail.next = newnode
        self.tail = newnode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < self.length:
            p = self.dummy
            q = self.dummy.next
            while index:
                p = p.next
                q = q.next
                index -= 1
            newnode = ListNode(val)
            p.next = newnode
            newnode.next = q
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.length - 1:
            return
        p = self.dummy
        q = self.dummy.next
        while index:
            p = p.next
            q = q.next
            index -= 1
        if not q.next:
            p.next = None
            self.tail = p
        else:
            r = q.next
            p.next = r
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)