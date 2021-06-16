class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        a, spread, border, flag = len(A), [], [], False
        for i in range(a):
            for j in range(a):
                if A[i][j]:  # 找到任一岛屿的起始点
                    A[i][j] = -1  # 置为已访问
                    spread.append((i, j))
                    flag = True
                    break
            if flag:
                break
        step = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while spread:  # bfs找该岛屿的所有部分
            i, j = spread.pop(0)
            neighbor = 0
            if i == 0 or i == a-1:
                neighbor += 1
            if j == 0 or j == a-1:
                neighbor += 1
            for di, dj in step:
                _i, _j = i+di, j+dj
                if -1 < _i < a and -1 < _j < a:
                    if A[_i][_j] == 1:
                        neighbor += 1
                        A[_i][_j] = -1  # 置为已访问
                        spread.append((_i, _j))  # 加入队列
                    elif A[_i][_j] == -1:
                        neighbor += 1
            if neighbor < 4:  # 邻居小于4则该坐标为岛屿边界点
                border.append((i, j, 0))
        while True:  # 对边界点进行BFS扩散
            i, j, n = border.pop(0)
            for di, dj in step:
                _i, _j = i+di, j+dj
                if -1 < _i < a and -1 < _j < a:
                    if not A[_i][_j]:  # 仅当该位置为0才加入队列
                        A[_i][_j] = -1  # 置为已访问
                        border.append((_i, _j, n+1))
                    elif A[_i][_j] == 1:  # 为1则找到，为-1则跳过
                        return n


class Solution:
    def shortestBridge(self, A):

        row, col = len(A), len(A[0])
        visited = [[0] * col for _ in range(row)]  # 负责记录其中的一个岛
        q = []
        start = []  # 保存其中一个岛的所有位置
        found = False
        for i in range(row):  # 先找到一个岛中其中一个位置
            for j in range(col):
                if A[i][j] == 1:
                    found = True
                    q.append((i, j))
                    visited[i][j] = 1
                    break
            if found:
                break

        while q:  # 以其中一个岛的位置为基础，使用广度优先搜索方法，继续找到这个岛的其他位置
            tmp = []
            for a in q:
                x, y = a[0], a[1]
                start.append(a)  # 把岛的位置放到 start 队列里面
                if (x - 1 >= 0) and (visited[x - 1][y] == 0) and (A[x - 1][y] == 1):
                    tmp.append((x - 1, y))
                    visited[x - 1][y] = 1
                if (x + 1 < col) and (visited[x + 1][y] == 0) and (A[x + 1][y] == 1):
                    tmp.append((x + 1, y))
                    visited[x + 1][y] = 1
                if (y - 1 >= 0) and (visited[x][y - 1] == 0) and (A[x][y - 1] == 1):
                    tmp.append((x, y - 1))
                    visited[x][y - 1] = 1
                if (y + 1 < row) and (visited[x][y + 1] == 0) and (A[x][y + 1] == 1):
                    tmp.append((x, y + 1))
                    visited[x][y + 1] = 1
            q = tmp

        ans = 0
        while start:  # 从一个岛出发，去找探索另外一个岛
            tmp = []
            for a in start:  # 广度优先算法，一层一层的探查 是否 到达另外一个岛
                x, y = a[0], a[1]
                if (x - 1 >= 0) and (visited[x - 1][y] == 0):
                    if A[x - 1][y] == 1:
                        return ans
                    else:
                        tmp.append((x - 1, y))
                        visited[x - 1][y] = 1
                if (x + 1 < col) and (visited[x + 1][y] == 0):
                    if A[x + 1][y] == 1:
                        return ans
                    else:
                        tmp.append((x + 1, y))
                        visited[x + 1][y] = 1
                if (y - 1 >= 0) and (visited[x][y - 1] == 0):
                    if A[x][y - 1] == 1:
                        return ans
                    else:
                        tmp.append((x, y - 1))
                        visited[x][y - 1] = 1
                if (y + 1 < row) and (visited[x][y + 1] == 0):
                    if A[x][y + 1] == 1:
                        return ans
                    else:
                        tmp.append((x, y + 1))
                        visited[x][y + 1] = 1

            start = tmp  # 探索了一层之后，没有发现另外一个岛，则，更新 最外层边界 以及 路径长度
            ans += 1

        return ans


