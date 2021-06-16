

#动态规划：完全背包问题
class Solution:
    def coinChange(self, coins, m):
        dp = [float('inf')] * (m+1)
        dp[0] = 0
        for coin in coins:# 枚举硬币种数
            for j in range(coin,m+1):# 从小到大枚举金额，确保j-c >= 0.
                dp[j] = min(dp[j-coin]+1, dp[j])
        return dp[m] if dp[m] != float('inf') else -1# 如果为inf说明状态不可达，返回-1即可。


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.res = float("inf")

        def dfs(i, num, amount):
            if amount == 0:
                self.res = min(self.res, num)
                return
            for j in range(i, len(coins)):
                # 剩下的最大值都不够凑出来了
                if (self.res - num) * coins[j] < amount:
                    break
                if coins[j] > amount:
                    continue
                dfs(j, num + 1, amount - coins[j])

        for i in range(len(coins)):
            dfs(i, 0, amount)

        return self.res if self.res != float("inf") else -1



#BFS
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import deque
        queue = deque([amount])
        step = 0
        visited = set()
        while queue:
            n = len(queue)
            for _ in range(n):
                tmp = queue.pop()
                if tmp == 0:
                    return step
                for coin in coins:
                    if tmp >= coin and tmp - coin not in visited:
                        visited.add(tmp - coin)
                        queue.appendleft(tmp - coin)
            step += 1
        return -1