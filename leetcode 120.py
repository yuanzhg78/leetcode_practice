class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        res=triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                res[j]=min[res[j],res[j+1]]+triangle[i][j]
        return res[0]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        三角型二维数组：m*n
        DP状态定义：dp[i, j]指从下面一层走到当前层，路径和的最小值
        DP状态方程：dp[i, j] = min(dp(i+1, j), dp(i+1, j+1)) + triangle[i, j]
        DP初始状态: dp[m-1, j] = Triangle[m-1, j]
          注意这里比较的不是数组元素值，而是路径和
          最后一直递推到dp[0, 0]就是我们要的值了

        """
        if not triangle:
            return 0

        # res指三角形最下面的一层，既是triangle数组里的元素，又是当前的最小路径
        res = triangle[-1]

        # 状态转移是从倒数第二行开始的（也就是递推的顺序）
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
                # 上面这一行代码用到了状态压缩的思路，其实就是数组复用而已，因为数组元素用过一次后就用不着了，接着被状态值覆盖掉，这一可以省去不少空间。
        return res[0]

#https://leetcode-cn.com/problems/triangle/solution/dong-tai-gui-hua-onkong-jian-by-powcai/

def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        # 建dp空间
        dp = [[0] * i for i in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for k in range(i + 1):
                if k == 0:
                    dp[i][k] = dp[i - 1][k] + triangle[i][k]
                elif k == i:
                    dp[i][k] = dp[i - 1][k - 1] + triangle[i][k]
                else:
                    dp[i][k] = min(dp[i - 1][k - 1], dp[i - 1][k]) + triangle[i][k]
        return min(dp[-1])

def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        dp = [0] * row
        for i in range(len(triangle[-1])):
            dp[i] = triangle[-1][i]
        # print(dp)
        for i in range(row - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


