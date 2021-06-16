#动态规划自下而上（自底而上）
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # n为格子的列数，m为格子的行数
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        #使用数组dp保存起点到任意点的路径数
        dp = [[0 for i in range(n)] for i in range(m)]#先列再行
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    # 如果[i,j]是障碍物，则dp[i][j]=0
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    # 如果[i,j]是起点，则dp[i][j]=1
                    dp[i][j] = 1
                else:
                    # 因为机器人只能往下或者往右移动
                    # 得到动态方程，如下
                    #     dp[i][j] = dp[i-1][j] + dp[i][j-1] （i>1,j>1）
                    #     且当i=0时，dp[i][j] = dp[i][j-1]
                    #       当j=0时，dp[i][j] = dp[i-1][j]
                    if i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        #dp[i][j] = dp[i-1][j] + dp[i][j-1] （i>1,j>1）
                        dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]











class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        动态规划（自底向上）
        """
        # m代表格子的列数，n代表格子的行数
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        # 创建一个数组r 用于保存所有子问题的解
        r = [[0] * m for _ in range(n)]
        # 一行一行构建从起点[0,0]到点[i,j]的路径数
        for i in range(0, n):
            for j in range(0, m):
                # 如果[i,j]是障碍物，则r[i][j]=0
                if obstacleGrid[i][j] == 1:
                    r[i][j] = 0
                # 如果[i,j]是起点，则r[i][j]=1
                elif i == 0 and j == 0:
                    r[i][j] = 1
                else:
                    # 因为机器人只能往下或者往右移动
                    # 得到动态方程，如下
                    #     r[i][j] = r[i-1][j] + r[i][j-1] （i>1,j>1）
                    #     且当i=0时，r[i][j] = r[i][j-1]
                    #       当j=0时，r[i][j] = r[i-1][j]
                    if i == 0:
                        r[i][j] = r[i][j - 1]
                    elif j == 0:
                        r[i][j] = r[i - 1][j]
                    else:
                        r[i][j] = r[i - 1][j] + r[i][j - 1]

        return r[n - 1][m - 1]
