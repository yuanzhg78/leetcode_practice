#并查集 介绍
#https://blog.csdn.net/weixin_42092787/article/details/106639060?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.control&spm=1001.2101.3001.4242
class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        tmp = {chr(i): chr(i) for i in range(97, 125)}

        def find(x):
            if x != tmp[x]:
                tmp[x] = find(tmp[x])
            return tmp[x]

        for i in range(len(A)):
            a, b = find(A[i]), find(B[i])
            if a < b:
                tmp[b] = a
            else:
                tmp[a] = b

        res = ""
        for c in S:
            res += tmp[find(c)]

        return res
'''
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b"或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。
'''
'''
# 输入：["a==b","b!=a"]
# 输出：false
# 解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
'''
#这个问题一看就是并查集问题，所以直接使用并查集就过了。将所有相等的元素构成一个集合中，然后判断不相等的元素是不是相同根即可。

class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        tmp = {chr(i): chr(i) for i in range(97, 125)}

        def find(x):
            if x != tmp[x]:
                tmp[x] = find(tmp[x])
            return tmp[x]

        for it in equations:
            if it[1] == '=':
                tmp[find(it[0])] = find(it[-1])

        for it in equations:
            if it[1] == '!':
                if find(it[0]) == find(it[-1]):
                    return False
        return True


class DSU:
    def __init__(self, n: int):
        self._n = n
        self._array = [i for i in range(n)]
        self._size = [1] * n

    def find(self, i: int) -> int:
        if self._array[i] != i:
            self._array[i] = self.find(self._array[i])
        return self._array[i]

    def union(self, i: int, j: int) -> bool:
        i, j = self.find(i), self.find(j)
        if i != j:
            if i < j:
                self._array[j] = i
            else:
                self._array[i] = j
            return True
        else:
            return False

    def is_connected(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)

    @property
    def group_num(self):
        """计算连通分支数量"""
        return len(set(self._array))

    @property
    def max_group_size(self):
        """计算最大连通分支包含的数量"""
        import collections
        return max(collections.Counter(self._array).values())


class Solution:
    def smallestEquivalentString(self, a: str, b: str, s: str) -> str:
        size1, size2 = len(a), len(s)

        dsu = DSU(26)

        for i in range(size1):
            dsu.union(ord(a[i]) - 97, ord(b[i]) - 97)

        ans = []
        for i in range(size2):
            ans.append(chr(dsu.find(ord(s[i]) - 97) + 97))
        return "".join(ans)
