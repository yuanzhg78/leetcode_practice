#https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/ha-xi-biao-zhu-xing-jie-shi-python3-by-zhu_shi_fu/
#用COUNTER
from collections import Counter
class Solution:
    def subarraySum(self, nums, k):
        tmp = Counter()
        cur = 0
        res = 0
        for i in range(len(nums)):
            cur += nums[i]
            res += tmp[cur-k]
            tmp[cur] += 1
            if cur == k:
                res += 1
        return res
if __name__ == "__main__":
    nums=[2,7,11,15]
    print(Solution().subarraySum([2,4],6))