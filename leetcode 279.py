#BFS
class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        if n == 0:
            return 0
        queue = deque([n])
        step = 0
        visited = set()#标记已经visited的点
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                tmp = queue.pop()
                for i in range(1, int(tmp ** 0.5) + 1):
                    diff = tmp - i ** 2
                    if diff == 0:
                        return step
                    if diff not in visited:#如果没有visited 加入到set中，将临接的点加入队列中
                        visited.add(diff)
                        queue.appendleft(diff)
        return step


#bfs是按一层一层来访问的，所以适合有目标求最短路的步数，你想想层层搜索每次层就代表了一步。bfs优先访问的是兄弟节点，只有这一层全部访问完才能访问下一层，
# 也就是说bfs第几层就代表当前可以走到的位置(结点).而dfs是按递归来实现的，它优先搜索深度，再回溯，优先访问的是没有访问过的子节点


