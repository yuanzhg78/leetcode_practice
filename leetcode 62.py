class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return pre[-1]


class Solution: #空间复杂度O(n)
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]



class Solution:#普通 空间复杂度O(mn)
    def uniquePaths(self, m: int, n: int) -> int:
            res=[[1 for i in range(n)] for i in range(m)]  #m与n的位置别弄反了，m是行，n是列，第一行，第一列初始值都赋值为1
            for i in range(1,m):
                        for j in range(1,n):
                            res[i][j]=res[i-1][j]+res[i][j-1]
            return res[m-1][n-1]
