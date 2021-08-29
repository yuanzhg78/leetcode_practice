#会员题目
#杀掉进程
#https://blog.csdn.net/weixin_30279315/article/details/97515072?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control
# Input:
# pid =  [1, 3, 10, 5]
# ppid = [3, 0, 5, 3] 父进程数组
# kill = 5
# Output: [5,10]
#构建父进程及其所有子进程的映射 需要用hash。先把把要结束的进程放入结果中，然后将所有子进程以及以下的进程放入结果中。
from collections import defaultdict,deque
#dfs
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int] 父进程
        :type kill: int
        :rtype: List[int]
        """
        def killAll(pid, children, killed):
            killed.append(pid)
            for child in children[pid]:
                killAll(child, children, killed)

        result = []
        children = defaultdict(set)
        for i in range(len(pid)): #也可以默认为list append
            children[ppid[i]].add(pid[i])
        killAll(kill, children, result)
        return result

#BFS
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        result = []
        children = defaultdict(set)
        for i in range(len(pid)):
            children[ppid[i]].add(pid[i])
        # BFS
        q = deque()
        q.append(kill)
        while q:
            p = q.popleft()
            result.append(p)
            for child in children[p]:
                q.append(child)
        return result