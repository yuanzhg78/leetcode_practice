# 中位数
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #二维数组的异常判断
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        row, col = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row.append(i)
                    col.append(j)
        meet_point = [self.findMedian(row), self.findMedian(col)]

        res = 0
        #计算每个点到中位数
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    # 计算曼哈顿距离
                    res += abs(i - meet_point[0]) + abs(j - meet_point[1])
        return res

    def findMedian(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


# 先考虑一维的情况，如果所有人都住在一条直线上，想要找到使总行走距离最小的一个见面点，
# 这个见面点应当设置为所有人居住位置的中位数。
# 推广到二维，其实就是横向找一个中位数，再纵向找一个中位数，即可得到最佳见面点，
# 然后计算每个人到见面点的距离即可。