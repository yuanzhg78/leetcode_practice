from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

#
# 我们用两个堆， 一个最小堆，一个最大堆
#
# 我们把数据分成两部分，求中位数就是前半部分的最大值，后半部分的最小值。
#
# 当数据流为奇数个时候，说明最小堆个数，和最大堆个数要不一样，我们把这个数放在哪个堆里，其实都一样的，这里我放在后半部分（最小堆）
#
# 我们每次入堆，都有从另一个堆里挤出一个元素，保证最小堆和最大堆是数据流前后两部分
#
# 插入时间复杂度：O(log(n))
#
# 查找：O(1)


