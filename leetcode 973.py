#快速排序
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 计算欧几里得距离
        distance = lambda i: points[i][0] ** 2 + points[i][1] ** 2

        def work(i, j, K):
            if i > j:
                return
            # 记录初始值
            oi, oj = i, j
            # 取最左边为哨兵值
            pivot = distance(oi)
            while i != j:
                while i < j and distance(j) >= pivot:
                    j -= 1
                while i < j and distance(i) <= pivot:
                    i += 1
                if i < j:
                    # 交换值
                    points[i], points[j] = points[j], points[i]

                    # 交换哨兵
            points[i], points[oi] = points[oi], points[i]

            # 递归
            if K <= i - oi + 1:
                # 左半边排序
                work(oi, i - 1, K)
            else:
                # 右半边排序
                work(i + 1, oj, K - (i - oi + 1))

        work(0, len(points) - 1, K)
        return points[:K]

#堆 （类似于top k 用的小根堆）此处用大根堆

from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        queue = []
        distance = lambda x: points[x][0]**2 + points[x][1]**2
        length = len(points)
        for i in range(length):
            heappush(queue, (distance(i), points[i]))
        res = []
        for i in range(K):
            res.append(heappop(queue)[1]) #从堆中弹出最小值重复k次
        return res


from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = []
        for point in points:
            heappush(distance, (point[0] ** 2 + point[1] ** 2, point))
        res = []
        for i in range(K):
            res.append(heappop(distance)[1])
        return res
#minimum Heap:
#make a maximum-heap to store distance, (point's distance to original, point)
#each time call heappop (distance), it will pop the smallest item in the heap. So heappop K times will be the result.
# Time complexity: O(nlogn)
# heapq is a binary heap, with O(log n) push and O(log n) pop.
# In the process, we did O(nlogn) heappush and O(klogk) heappop.
# so the time complexity would be O(nlogn).

