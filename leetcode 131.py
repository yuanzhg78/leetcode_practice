#Given a string s, partition s such that every substring of the partition is a palindrome.
#Return all possible palindrome partitioning of s.


class Solution:
    def partition(self, s):
        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                print(path[:])
                return
            for i in range(1, len(s) + 1):
                if s[:i] == s[i - 1::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, res)
                    path.pop()

        res = []
        dfs(s, [], res)
        return res
if __name__ == "__main__":
        s = 'aab'
        res = Solution().partition(s)
        print(res)

class Solution:
    def partition(self, s):
        res=[]
        def dfs(s,path,res):
            if not s:
                re




from typing import List
class Solution:
    def partition1(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False]*n for c in range(n)]
        for i in range(n):
            for j in range(i+1):
                if (s[i]==s[j]) and (i-j<=2 or dp[j+1][i-1]):
                    dp[j][i]=True
        res=[]
        tmp=[]
        i=0
        def dfs(i,tmp):
            if i == n:
                res.append(tmp)
            for j in range(i,n):
                if dp[i][j]:
                    dfs((j+1),tmp+[s[i:j+1]])
        dfs(i,tmp)
        return  res



class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def dfs(s, path):
            if not s:
                res.append(path[:])
                return
            for i in range(1,len(s)+1):
                if s[:i] == s[:i][::-1]:
                    print(s[:i])
                    dfs(s[i:], path+[s[:i]])
        dfs(s, [])
        return res


if __name__ == "__main__":
        s = 'aab'
        res = Solution().partition(s)
        print(res)


#深度优先搜索(下面的程序）
#结束条件：搜索完整个字符串
#符合条件的子串：原本的子串和该子串逆序后相同，为回文子串。
#第三个过程比较详细
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1,len(s)+1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], path+[s[:i]], res)
        dfs(s, [],res)
        return res