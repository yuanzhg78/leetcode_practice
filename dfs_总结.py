class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def dfs(tmp, index):
            if index == len(digits):
                res.append(tmp)
                return
            char = digits[index]
            letters = d[ord(char) - 48]
            for i in letters:  # 遍历数字对应的字符串
                dfs(tmp + i, index + 1)

        dfs("", 0)
        return res




#DFS
#https://leetcode-cn.com/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'#将岛屿的所有节点删除，防止之后重复搜索岛屿
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count


# BFS是按一层一层来访问的，所以适合有目标求最短路的步数，你想想层层搜索每次层就代表了一步。bfs优先访问的是兄弟节点，只有这一层全部访问完才能访问下一层，也就是说bfs第几层就代表当前可以走到的位置(结点).
# 而dfs是按递归来实现的，它优先搜索深度，再回溯，优先访问的是没有访问过的子节点
#
# DFS多用于连通性问题因为其运行思想与人脑的思维很相似，故解决连通性问题更自然。BFS多用于解决最短路问题，其运行过程中需要储存每一层的信息，所以其运行时需要储存的信息量较大，如果人脑也可储存大量信息的话，理论上人脑也可运行BFS。
# 总的来说多数情况下运行BFS所需的内存会大于DFS需要的内存(DFS一次访问一条路，BFS一次访问多条路)，DFS容易爆栈(栈不易"控制")，BFS通过控制队列可以很好解决"爆队列"风险。
# 它们两者间各自的优势需要通过实际的问题来具体分析，根据它们各自的特点来应用于不同的问题中才能获得最优的性能。
#https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/
#https://leetcode-cn.com/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def bfs(grid, i, j):
            queue = [[i, j]]
            while queue:
                [i, j] = queue.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0': continue
                bfs(grid, i, j)
                count += 1
        return count


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':#不出边界才继续，已经是水就直接返回
                return
            grid[i][j] = '0'#将岛屿的所有节点删除，防止之后重复搜索岛屿，更新是陆地的区块，表示已经计算过
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        count = 0
        for i in range(len(grid)):#双层遍历
            for j in range(len(grid[0])):
                if grid[i][j] == '1':#如果是水就放过，如果是land就做dfs
                    dfs(grid, i, j)
                    count += 1
        return count
if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]

    solution = Solution()
    result = solution.numIslands(grid)
    print(result)



from typing import List


class Solution:
    #        x-1,y
    # x,y-1    x,y      x,y+1
    #        x+1,y
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        # 特判
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 DFS 发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j] == '1':
                    # count 可以理解为连通分量，你可以在深度优先遍历完成以后，再计数，
                    # 即这行代码放在【位置 1】也是可以的
                    count += 1
                    self.__dfs(grid, i, j, m, n, marked)
                    # 【位置 1】
        return count

    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.__dfs(grid, new_i, new_j, m, n, marked)


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)

#图像渲染 bfs
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        if image[sr][sc] ==  newColor:
            return image
        direct = {(1, 0), (-1, 0), (0, 1), (0, -1)} #元组
        queue = deque()
        queue.append([sr,sc])
        origin = image[sr][sc]
        while queue:
            sr,sc = queue.popleft()
            image[sr][sc] = newColor
            for d in direct:
                new_i = sr + d[0]
                new_j = sc + d[1]
                if 0 <= new_i < m and 0 <= new_j < n and image[new_i][new_j] == origin:
                    queue.append([new_i, new_j])
        return image

#并查集
class Solution:
    """并查集"""
    '''
    root 存放accounts里面每个节点的parent
    mail 存放每个邮箱地址的第一次出现parent
    '''

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        root = [i for i in range(len(accounts))]
        mail = {}

        # 并查集find
        def find(i):
            if root[i] != i:
                return find(root[i])
            return root[i]

        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email not in mail:
                    mail[email] = i
                else:
                    # 通过find找到i的最终parent，然后将parent的parent改写为mail通过find找到的parent
                    # 由于mail里存放的节点的父节点也可能被更新所以要通过find找到最终parent

                    root[find(i)] = find(mail[email])

        # 存放子账户
        delt = set()
        for i in range(len(root)):
            if root[i] != i:
                # 通过find找到i的最终parent，然后把i添加进最终parent
                accounts[find(root[i])].extend(accounts[i][1:])
                delt.add(i)
        # 筛选出不含子账户的最终账户存入result
        result = []
        for i in range(len(accounts)):
            if i not in delt:
                result.append(accounts[i][:1] + sorted(list(set(accounts[i][1:]))))
        return result