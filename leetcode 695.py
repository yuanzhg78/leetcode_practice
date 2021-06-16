class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Reset cur_area to 0
                    self.cur_area = 0
                    self.dfs(grid, i, j)

                    max_area = max(max_area, self.cur_area)

        return max_area

    def dfs(self, grid, i, j):
        self.cur_area += 1
        grid[i][j] = '#'

        # Check left
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            self.dfs(grid, i, j - 1)

        # Check right
        if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
            self.dfs(grid, i, j + 1)

        # Check up
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            self.dfs(grid, i - 1, j)

        # Check down
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            self.dfs(grid, i + 1, j)




class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        x_length=len(grid)
        y_length=len(grid[0])
        vis=[[1 for j in range(y_length)] for i in range(x_length)]
        def DFS(i,j,vis=vis):
            if i>=0 and i<x_length and j>=0 and j<y_length and vis[i][j]==1 and grid[i][j]==1 :
                vis[i][j]=0
                res=DFS(i-1,j)+DFS(i+1,j)+DFS(i,j-1)+DFS(i,j+1)+1
                # print i,j,res
                return res
            else:
                return 0
        res=[0]
        for i in range(x_length):
            for j in range(y_length):
                if vis[i][j]==1 and grid[i][j]==1:
                    val=DFS(i,j,vis=vis)
                    # print i, j, val, vis

                    res.append(val)

        return max(res)

#后两个容易理解
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        这里和前面不一样的是需要存储size，所以给递归函数需要一个返回值，（不要用全局变量）
        """
        max_area = 0
        res = 0

        def infect(grid, i, j):

            ''' 这个是DFS函数，一般不用修改，功能就是遍历和(i,j)相连的所有格子'''

            # 遇到边界，或者不是1的地方就返回
            if (i < 0 or i >= len(grid) or j < 0
                    or j >= len(grid[0]) or grid[i][j] != 1
            ):
                return 0
            grid[i][j] = 2
            return 1 + infect(grid, i, j + 1) + infect(grid, i, j - 1) + infect(grid, i + 1, j) + infect(grid, i - 1, j)

        #        也可以像下面这样分开写
        #            res=1
        #            往四周感染
        #            res+=infect(grid,i,j+1)
        #            res+=infect(grid,i,j-1)
        #            res+=infect(grid,i+1,j)
        #            res+=infect(grid,i-1,j)
        #            return res

        # 主函数
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                self.size = 0
                if (grid[i][j] == 1):
                    res = infect(grid, i, j)  # 开始感染
                    max_area = max(res, max_area)
        return max_area




class Solution(object):
    def maxAreaOfIsland(self, grid):
        row = len(grid)
        low = len(grid[0])
        rs = 0
        for i in range(row):
            for j in range(low):
                if grid[i][j] == 1:
                    temp = self.getArea(i,j,grid)
                    rs = max(rs, temp)

        pass

    def getArea(self, i, j, grid):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
            return 0
        rs = 1
        grid[i][j] = 0

        rs += self.getArea(i-1, j, grid)
        rs += self.getArea(i+1, j, grid)
        rs += self.getArea(i, j-1, grid)
        rs += self.getArea(i, j+1, grid)

        return rs
