
# Author: Huahua
from functools import lru_cache
class Solution:
  def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    mod = 10 ** 9 + 7    
    # Number of ways to have target t using i dices.
    @lru_cache(maxsize=None)
    def dp(i, t):
      if i == 0: return 1 if t == 0 else 0
      # Pruning 388 ms -> 132 ms
      if t > f * i or t < i: return 0
      ans = 0
      for k in range(1, f + 1):
        ans = (ans + dp(i - 1, t - k)) % mod
      return ans    
    return dp(d, target)

  class Solution:
      def numRollsToTarget(self, d: int, f: int, target: int) -> int:
          dp = [[0 for i in range(target + 1)] for j in range(d)]

          for i in range(f):
              if i + 1 <= target:
                  dp[0][i + 1] = 1

          for i in range(1, d):
              for j in range(1, target + 1):
                  k = 1
                  while j - k > 0 and k <= f:
                      dp[i][j] += dp[i - 1][j - k]
                      k += 1

          return dp[-1][-1] % (10**9 + 7)



