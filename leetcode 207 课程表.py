class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjaency = [[] for _ in range(numCourses)]
        queue = []
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjaency[pre].append(cur)

        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjaency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses


# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

'''
解题思路：
本题可约化为： 课程安排图是否是 有向无环图(DAG)。即课程间规定了前置条件，但不能构成任何环路，否则课程前置条件将不成立。
思路是通过 拓扑排序 判断此课程安排图是否是 有向无环图(DAG) 。 拓扑排序原理： 对 DAG 的顶点进行排序，使得对每一条有向边 (u, v)(u,v)，均有 uu（在排序记录中）比 vv 先出现。亦可理解为对某点 vv 而言，只有当 vv 的所有源点均出现了，vv 才能出现。
通过课程前置条件列表 prerequisites 可以得到课程安排图的 邻接表 adjacency，以降低算法时间复杂度，以下两种方法都会用到邻接表。
'''

'''
算法流程：
1 统计课程安排图中每个节点的入度，生成 入度表 indegrees。
2 借助一个队列 queue，将所有入度为 0 的节点入队。
3 当 queue 非空时，依次将队首节点出队，在课程安排图中删除此节点 pre：
并不是真正从邻接表中删除此节点 pre，而是将此节点对应所有邻接节点 cur 的入度 -1，即 indegrees[cur] -= 1。
当入度 -1后邻接节点 cur 的入度为 0，说明 cur 所有的前驱节点已经被 “删除”，此时将 cur 入队。
4 在每次 pre 出队时，执行 numCourses--；
41若整个课程安排图是有向无环图（即可以安排），则所有节点一定都入队并出队过，即完成拓扑排序。换个角度说，若课程安排图中存在环，一定有节点的入度始终不为 0。
42因此，拓扑排序出队次数等于课程个数，返回 numCourses = 0 判断课程是否可以成功安排。

'''