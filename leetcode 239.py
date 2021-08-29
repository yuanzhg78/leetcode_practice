# 双端队列记录滑动窗口中元素的索引，队列左边界记录当前滑动窗口中最大元素的索引
# 遍历数组，当前元素为 num，索引为 i
# 当队列非空，左边界出界时（滑动窗口向右移导致的），更新左边界
# 当队列非空，将队列中索引对应的元素值比 num 小的移除
# 更新队列
# 当索引 i 大于 k-1，更新输出结果
from collections import deque
import heapq
class Solution:
    #单调队列
    def maxSlidingWindow(self, nums, k):
        que = deque()
        res = []
        for i in range(len(nums)):
            while que and nums[que[-1]] <= nums[i]: #队列不空，且新增加的右端值大于队列尾，删除队列内小的值。
                que.pop()
            que.append(i)       #直接添加右端值，因为已经为队列内最小值了
            if que and que[0] < i - k + 1:  #如果左端最大值不在窗口范围，删除
                que.popleft()
            if i + 1 >= k:      #从窗口满足K时开始添加到结果
                res.append(nums[que[0]])
        return res

#python 小根堆介绍
#https://www.jianshu.com/p/801318c77ab5
#https://blog.csdn.net/lady_killer9/article/details/111998013?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1.control&spm=1001.2101.3001.4242
# python默认是小根堆，故加"-"，形成"大根堆"
# 由于堆顶元素可能不在滑动窗口内，故要维护一个二元组(num, index)
# 通过index判断堆顶元素是否在滑动窗口内
# 首先把 k 个元素加入大根堆

#判断栈顶元素下标是否在窗口内
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # nums = [1, 3, -1, -3, 5, 3, 6, 7]
        # how to get max value among the window
        # use maximum heap (-value, index)

        # Time complexity : O(NlogN)
        # Space complexity: O(N)
        res, heap = [], []
        for i in range(len(nums)):
            heapq.heappush(heap, ( -nums[i], i))
            if i + 1 >= k:
                while heap and heap[0][1] <  i + 1 - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res


# >>> from heapq import *
# >>> heap = [2,7,4,1,8,1]
# >>> heapify(heap)
# >>> print(type(heap),heap)
# <class 'list'> [1, 1, 2, 7, 8, 4]


#有 1000 个无序的整数，希望使用最快的方式找出前 50 个最大的

import heapq
def heapsort(data, hp_size=3):
    h = []
    for i in range(len(data)):
        if i >= hp_size:
            #先push再pop
            heapq.heappushpop(h, data[i])
        else:
            heapq.heappush(h, data[i])
    return [heapq.heappop(h) for _ in range(len(h))]

res = heapsort([6,2,1,-4,9,4,0])
print(res)


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #初始化tem和存放结果的列表
        tem, res = [], []
        for i, x in enumerate(nums):
            # 维护tem大小为k
            if i >= k and tem[0] <= i - k:
                tem.pop(0)
            #将左侧比当前x值小的数据索引都清掉，维护左端最大
            while tem and nums[tem[-1]] <= x:
                tem.pop()
            tem.append(i)
            #将最大值放入res列表中
            if i >= k-1:
                res.append(nums[tem[0]])
        return res
