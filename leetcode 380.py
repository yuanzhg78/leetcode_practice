from random import choice


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # 插入时：用哈希表来判断是否已存在O(1)，数组末尾增加一个元素O(1)，哈希表记录｛值：索引｝O(1)
        # 已经存在的元素会提示插入失败
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # 哈希表用于存val对应的idx
        if val in self.dict:
            last = self.list[-1]  # get the last ele
            idx = self.dict[val]
            self.list[idx] = last  # 将要删除元素与最后一个元素交换

            # update hashtable
            self.dict[last] = idx

            # 字典中删除一个元素用del
            del self.dict[val]  # self.dict.pop(val)
            # update list del the last ele of the list
            self.list.pop()  # 删除最后一个元素。
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)
        # return self.b[random.randrange(0,self.length)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()